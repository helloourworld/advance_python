
# coding: utf-8

# In[5]:

daysInSolarMonth=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# In[6]:

lunarMonthDays  = [29,30] # a short (long) lunar month has 29 (30) days */


# In[7]:

shengXiaoEn     = ["Mouse", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
                   "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]


# In[8]:

shengXiaoGB     = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡",
                   "狗", "猪"]


# In[9]:

zhiGB           = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉",
                   "戌", "亥"]
ganGB           = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]


# In[10]:

monthEn         = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November',
                   'December']
weekdayEn       = ["Monday", "Tuesday", "Wednesday", "Thursday",
                   "Friday", "Saturday", "Sunday"]


# In[11]:

weekdayGB       = ["一", "二", "三", "四", "五", "六", "日"]
numGB           = ['○', "一", "二", "三", "四", "五", "六", "七", "八", "九",
                   "十"]
lunarHoliday    = {'0_0':'春节', '4_4':'端午', '7_14':'中秋', '8_8':'重阳',
                   '0_14':'元宵'}


# In[12]:

yearCode = [
         0x04bd8, # 1900
    0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950, # 1905
    0x16554, 0x056a0, 0x09ad0, 0x055d2, 0x04ae0, # 1910
    0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540, # 1915
    0x056a0, 0x0ada2, 0x095b0, 0x14977, 0x04970, # 1920
    0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54, # 1925
    0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566, # 1930
    0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60, # 1935
    0x186e3, 0x092e0, 0x1c8d7, 0x0c950, 0x0d4a0, # 1940
    0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0, # 1945
    0x092d0, 0x0d2b2, 0x0a950, 0x0b557, 0x06ca0, # 1950
    0x0b550, 0x15355, 0x04da0, 0x0a5b0, 0x14573, # 1955
    0x052b0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6, # 1960
    0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260, # 1965
    0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0, # 1970
    0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250, # 1975
    0x0d558, 0x0b540, 0x0b6a0, 0x195a6, 0x095b0, # 1980
    0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, # 1985
    0x06d40, 0x0af46, 0x0ab60, 0x09570, 0x04af5, # 1990
    0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58, # 1995
    0x055c0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960, # 2000
    0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0, # 2005
    0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950, # 2010
    0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0, # 2015
    0x0a5b0, 0x15176, 0x052b0, 0x0a930, 0x07954, # 2020
    0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6, # 2025
    0x0a4e0, 0x0d260, 0x0ea65, 0x0d530, 0x05aa0, # 2030
    0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0, # 2035
    0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0, # 2040
    0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0, # 2045
    0x0aa50, 0x1b255, 0x06d20, 0x0ada0   # 2049
]
yearsCoded = len(yearCode)


# In[13]:

from sys import argv, exit, stdout


# In[14]:

from time import time,localtime


# In[15]:

ow=stdout.write


# In[43]:

# #   The leap month (if exists) is long one if M = 1.
class LunarYearInfo:
    '''
    农历闰年
    中国旧历作为阴阳历的一种，每月的天数依照月亏而定，一年的时间以12个月为基准，平年
    比一回归年少约11天。为了合上地球围绕太阳运行周期即回归年，每隔2到4年，增加一个月，
    增加的这个月为闰月。闰月加到哪个月，以农历历法规则推断，主要依照与农历的二十四节
    气（春雨惊春清谷天，夏满芒夏暑相连，秋处露秋寒霜降，冬雪雪冬小大寒）相符合来确定。
    在加有闰月的那一年有13个月，历年长度为384或385日，这一年也称为闰年。如2015年羊年
    的农历中，有两个九月。农历闰年闰月的推算，3年一闰，5年二闰，19年七闰；农历基本上
    19年为一周期对应于公历同一时间。如公历的2001年5月27日、1982年5月27日和1963年5月27
    日这个日子，都是闰四月初五。
    '''
    def __init__(self):
        self.yearDays = 0
        self.monthDays = [0] * 13
        self.leapMonth = -1 # -1 means no lunar leap month
        


# In[17]:

yearInfo = [0] * yearsCoded # global variable
for i in range(yearsCoded):
    yearInfo[i] = LunarYearInfo()


# In[18]:

class Date:
    def __init__(self, year, month, day, weekday=-1, gan=-1, zhi=-1):
        self.year = year
        self.month = month
        self.day = day
        self.weekday = weekday
        self.gan = gan
        self.zhi = zhi
        


# In[19]:

solar1st = Date(0, 0, 30, weekday=2) #Wednesday, 31Jan1900
lunar1st = Date(0, 0, 0, weekday=2, gan=6, zhi=0) #Wednesday, First day, First month, 1900,庚子年


# In[20]:

def error(msg):
    print 'Error:', msg; exit(0)


# In[21]:

def isSolarLeapYear(year):
    '''
    Leap year, Intercalary Year(闰年)是为了弥补因人为历法规定造成的年度天数与地球实际公转周期的时间差而设立的。补上时间差的年份为闰年。
    闰年包括在公历或夏历中有闰日或闰月的年份。
    闰年法则：四年一闰，百年不闰，四百年再闰
    根本原因：
    地球绕太阳运行周期为365天5小时48分46秒（合365.24219天)，即一回归年（tropical year）。公历的平年只有365日，比回归年短约0.2422日，所余下的时间约为每四年
    累计一天，故第四年于2月末加一天，使当年的历年长度为366日，这一年为闰年。
    现行公历中每400年有97个闰年。
    按照每四年一个闰年计算，平均每年就要多算出0.0078天，这样经过400年就会多算出大约3天来。因此每四百年中要减少三个闰年。所以公历规定：年份是整百数时，必须
    是400的倍数才是闰年；不是400的倍数的年份，即使是4的倍数也不是闰年。
    '''
    year = year + 1900
    return (year%4==0) and (year%100!=0) or (year%400 ==0)
# isSolarLeapYear(108)


# In[23]:

baseYear=1201 - 1900
# in fact, real baseYear=1201.  In order to ease calculation of
# leap years. real baseYear must conform to:
#   realBaseYear%4==1 and realBaseYear%400==1.
# Assert realBaseYear < solar1st.year .
# Compute the number of days from the Solar First Date
# month=0 means January, ...


# In[24]:

def solarDaysFromBaseYear(d): # d is a Date class
    delta = d.year - baseYear
    offset = delta*365 + delta/4 - delta/100 + delta/400
    for i in range(d.month):
        offset += daysInSolarMonth[i];
    if d.month>1 and isSolarLeapYear(d.year):
        offset+=1
    offset += d.day
    return offset


# In[25]:

def solarDaysFromFirstDate (d): #d is a Date class
    return solarDaysFromBaseYear (d) - solarDaysFromBaseYear (solar1st)


# In[26]:

def calcLunarDaysPerMonth(iYear):
    code = yearCode[iYear]
    leapMonth = code&0xf #leapMonth==0 means no lunar leap month
    code >>= 4
    for iMonth in range(12):
        yearInfo[iYear].monthDays[11-iMonth] = lunarMonthDays [code&0x1]
        code >>= 1
    if leapMonth>0:
        yearInfo[iYear].leapMonth = leapMonth-1
        yearInfo[iYear].monthDays.insert (leapMonth,
                lunarMonthDays [code & 0x1])


# In[27]:

def calcAllLunarYearsInfo():
    for iYear in range(yearsCoded):
        calcLunarDaysPerMonth(iYear)
        for iMonth in range(13):
            yearInfo[iYear].yearDays += yearInfo[iYear].monthDays[iMonth]


# In[29]:

#input dateSolar, return (dateLunar, isLunarMonthOrNot)
def solar2Lunar(d): #d is a Date class
    dLunar = Date(-1, -1, -1) #unknown lunar Date class
    offset = solarDaysFromFirstDate(d)
    dLunar.weekday  = (offset + solar1st.weekday)%7
    for iYear in range(yearsCoded):
        if offset < yearInfo[iYear].yearDays:
            dLunar.year = iYear; break
    offset -= yearInfo[iYear].yearDays
    if dLunar.year == -1:   error ("Date out of range.")
    dLunar.gan      = (dLunar.year + lunar1st.gan) % 10
    dLunar.zhi      = (dLunar.year + lunar1st.zhi) % 12
    for iMonth in range(13):
        if offset< yearInfo[dLunar.year].monthDays[iMonth]:
            dLunar.month = iMonth; break
    offset -= yearInfo[dLunar.year].monthDays[iMonth]
    dLunar.day = offset

    isLeapMonth=0
    if yearInfo[dLunar.year].leapMonth >=0:
        if dLunar.month ==  yearInfo[iYear].leapMonth + 1:
            isLeapMonth=1
        if dLunar.month > yearInfo[dLunar.year].leapMonth:
            dLunar.month -= 1
    return (dLunar, isLeapMonth)


# In[30]:

def getSolarDaysInMonth (year, month):
    if isSolarLeapYear(year) and month==1:
            return 29
    else:   return daysInSolarMonth[month]


# In[31]:

getSolarDaysInMonth(2016, 1)


# In[32]:

def num2GB (num):
    if num==10:
        return '十'
    elif num>10 and num<20:
        return '十' + numGB[num-10]
    tmp=''
    while num>10:
        tmp = numGB[num%10] + tmp
        num = int(num/10)
    tmp = numGB[num] + tmp
    return tmp


# In[33]:

print num2GB(2)


# In[34]:

def lunarDate2GB (dLunar, isLeapMonth):
    tmp = str(dLunar.month)+'_'+str(dLunar.day)
    if lunarHoliday.has_key( tmp ):
        return '[0;33;44m%s[0m  '% lunarHoliday[tmp] +                ' '*(6-len(lunarHoliday[tmp]))
    elif dLunar.day==0:
        tmp2 = '闰'*isLeapMonth + num2GB(dLunar.month+1) +'月'
        return '[7m%s[0m' % tmp2 + ' '*(8-len(tmp2))
    elif dLunar.day<10:
        return '初' + num2GB(dLunar.day+1)
    else:
        return num2GB(dLunar.day+1)


# In[35]:

def outputCalendar(year, month):
    dLunar = Date(-1,-1,-1)
    ow ('\n     阳历%d年%d月         ' % (year+1900, month+1) )
    for iDay in range( getSolarDaysInMonth(year, month) ):
        dSolar = Date(year, month, iDay)
        dLunar, isLeapMonth = solar2Lunar (dSolar)
        if iDay==0:
            ow ('始于 阴历%s年%s%s月 (%s%s年, 生肖属%s)\n' %
                ( num2GB(dLunar.year+1900), '闰'*isLeapMonth,
                  num2GB(dLunar.month+1),
                  ganGB [dLunar.gan], zhiGB[dLunar.zhi], shengXiaoGB[dLunar.zhi]
                ))
            ow ('='*74 + '\n')
            for i in range(7):
                ow ("%3s %2s     " % (weekdayEn[i][:3], weekdayGB[i]) )
            ow('\n\n')
            for i in range(dLunar.weekday): ow(' '*11)
        elif dLunar.weekday==0: ow('\n')
        ow ( "%2d %-8s" %(iDay+1, lunarDate2GB(dLunar, isLeapMonth) ) )
    ow('\n\n')


# In[36]:

def checkArgv (argv):
    argc = len(argv)
    if argc==1 or argv[1] in ('-h', '--help'):
        print __doc__; exit(0)
    #in case people input arguments as "4-digit-year month"
    if argc==3 and len(argv[1]) == 4 and len(argv[2]) in (1,2):
        argv[1], argv[2] = argv[2], argv[1]

    #Get month
    month=-1
    for iMonth in range(12):
        if argv[1].lower() == monthEn[iMonth].lower() or            argv[1].lower() == monthEn[iMonth][:3].lower():
               month = iMonth+1; break
    if month==-1:
        month = eval(argv[1])
    if month<1 or month>12:     error ("Month not within 1--12.")
    #Get year
    if argc==2: year = localtime(time())[0]
    else:
        if len(argv[2]) != 4:   error ("Year must be 4 digits.")
        year = eval(argv[2])
        if year<1900 or year>= 1900+yearsCoded or (year==1900 and month==1):
            error ("Year must be within %d--%d, excluding 1900/1."
                    % (1900, 1900 + yearsCoded-1) )
    return year-1900, month-1


# In[40]:

yearInfo[1].monthDays


# In[ ]:



