#!/usr/bin/env python
# -*- coding: utf-8 -*-


# coding: utf-8

## Customer Churn Prediction

# In this webinar, we will loads data from the UCI Online Retail data (http://archive.ics.uci.edu/ml/datasets/Online+Retail) and predicts which customers are likely to churn given their purchase activity.
# 
# Churn can be defined in many ways. We define churn to be <b>no activity within a period of time (called the churn_period)</b>. Using this definition, a user/customer is said to have churned any form of activity is followed by no activity for an entire duration of time known as the `churn_period` (by default, we assume 30 days). The following figure better illustrates this concept.
# 
# <img src="https://turi.com/images/learn/churn-illustration.png"/>
# 
# (from our user guide: https://turi.com/learn/userguide/churn_prediction/churn-prediction.html)
# 
# We will dig deaper into the different parameters of the Churn Prediction toolkit, but let's start by loading some data!

# In[1]:

# Let's import Graphlab Create and a few other libraries
import graphlab as gl
import graphlab.aggregate
import datetime
import time


# ### Import data from a locally downloaded copy of the UCI data set
# 
# Graphlab Create supports loading data from live databases, as well as from local files. In this case, since we're working with a fixed dataset, we will load it from disk.

# In[2]:

#Data can come directly from a SQL database, for this webinar, we will load from a local copy
data = gl.SFrame("https://static.turi.com/datasets/churn-prediction/online_retail.csv")
data


# We need to do some cleanup first. The Invoice ID and Description columns are not going to help the model, and should be removed.

# In[3]:

data = data.remove_columns(['InvoiceNo', 'Description'])
data


# Now we need to convert the InvoiceDate (which is a string) into a Python DateTime object

# In[4]:

import dateutil
from dateutil import parser
def string_time_to_datetime(x):
    import datetime
    import pytz
    return dateutil.parser.parse(x)

data['InvoiceDate'] = data['InvoiceDate'].apply(string_time_to_datetime)


# Finally, we want to separate some users into a train/validation set, making sure the validation users are not in the training set, and creating TimeSeries objects out of them.

# In[5]:

(train, valid) = gl.churn_predictor.random_split(data, user_id = 'CustomerID', fraction = 0.9, seed = 12)
train_trial = gl.TimeSeries(train, index = 'InvoiceDate')
valid_trial = gl.TimeSeries(valid, index = 'InvoiceDate')


# Now we can load user information, which can be used to augment the churn prediction model.

# In[6]:

userdata = gl.SFrame("https://static.turi.com/datasets/churn-prediction/online_retail_side_data_extended.csv")
userdata


### Training the model

# Let's now train the model.

#### Create a train-test split based on users

# First, let's observe the data, and see what the time range looks like

# In[7]:

print "Start date : %s" % train_trial.min_time
print "End date   : %s" % train_trial.max_time


# In[8]:

# Period of inactivity that defines churn -- meaning that if a user stops purchasing
# items for 7 days, we'll consider them as having churned.
churn_period_trial = datetime.timedelta(days = 30) 

# Different beginning of months
churn_boundary_aug = datetime.datetime(year = 2011, month = 8, day = 1) 
churn_boundary_sep = datetime.datetime(year = 2011, month = 9, day = 1) 
churn_boundary_oct = datetime.datetime(year = 2011, month = 10, day = 1) 


# In[9]:

model = gl.churn_predictor.create(train_trial,
                                  user_data = userdata,
                                  user_id='CustomerID',
                                  churn_period = churn_period_trial,
                                  time_boundaries = [churn_boundary_aug, churn_boundary_sep, churn_boundary_oct])


#### Evaluating the model (post-hoc anaylsis)

# In[10]:

# Evaluate this model in October
evaluation_time = churn_boundary_oct


# In[11]:

metrics = model.evaluate(valid_trial, evaluation_time, user_data = userdata)


# In[12]:

print(metrics)


# In[13]:

# metrics['precision_recall_curve'].show()


#### Make predictions in the future

# Here the question to ask is will they churn after a certain period of time. To validate we can see if they user has used us after that evaluation period. Voila! I was confusing it with expiration time (customer churn not usage churn)

# In[14]:

# Make predictions in the future.

predictions_trial = model.predict(valid_trial, user_data = userdata)
predictions_trial.print_rows()


# In[15]:

predictions_trial.sort('probability', ascending=False).print_rows(20,max_column_width=20)


# In[16]:

predictions_trial.sort('probability', ascending=False)[200:300] .print_rows(20,max_column_width=20)


#### Inside the model

# In[17]:

model.trained_model


# In[18]:

model.trained_model.get_feature_importance()

