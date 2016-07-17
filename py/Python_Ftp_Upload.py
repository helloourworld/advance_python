# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:47:42 2016
@author: gouzhilong
"""

def Confirm_Files (results_dir):

    import os

    # 获取某目录下的所有内容（文件&子文件夹）
    list = os.listdir(results_dir)

    # 获取该目录下的文件列表
    filelist = []
    for i in range(0, len(list)):
        path = os.path.join(results_dir,list[i])
        if os.path.isfile(path):
            filelist.append(list[i])

    return(filelist)


def Last_Month_End_Day():

    import datetime
    LMLD = datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
    STR_LMLD = str(LMLD)[0:4]+str(LMLD)[5:7]+str(LMLD)[8:11]

    return(STR_LMLD)


def Ftp_Login(server, user, password, destination_dir, source_dir, filename):

    from ftplib import FTP

    ftp = FTP(); port = 21; timeout = 999
    ftp.set_debuglevel(2)                   #打开调试级别2，显示详细信息
    ftp.connect(server,port,timeout)        # 连接FTP服务器
    ftp.login(user, password)               # 登录
    print ftp.getwelcome()                  # 获得欢迎信息
    ftp.cwd(destination_dir)                # 设置FTP路径

    for i in xrange(len(filename)):
        bufsize = 1024
        file_handler = open(source_dir+filename[i],'rb')             #以读模式在本地打开文件
        ftp.storbinary('STOR '+filename[i], file_handler, bufsize)   # 上传FTP文件
        file_handler.close()
    ftp.set_debuglevel(0)

    list = ftp.nlst()                       # 获得目录列表
    print "\nAfter Ftp Upload, The Files is:"
    for name in list:
        print(name)                         # 打印文件名字

    ftp.quit()
    print "\nThe ModuleResult Upload is Success！"

    return()


if __name__ == '__main__':

    # 配置FTP参数
    server = '40.43.0.25'
    user = 'PYTHON_RISK_MODEL_USER'
    password = 'TC&6$3C4MOPWCN'
    destination_dir = '/' + Last_Month_End_Day() + ''
    # 确定上传目录及文件
    source_dir = 'C:/Machine_Learnning/Result_Data/'
    filename = Confirm_Files(source_dir)
    # 连接、上传
    Ftp_Login(server, user, password, destination_dir, source_dir, filename)













'''
ftp相关命令操作
ftp.cwd(pathname) #设置FTP当前操作的路径
ftp.dir() #显示目录下文件信息
ftp.nlst() #获取目录下的文件
ftp.mkd(pathname) #新建远程目录
ftp.pwd() #返回当前所在位置
ftp.rmd(dirname) #删除远程目录
ftp.delete(filename) #删除远程文件
ftp.rename(fromname, toname)#将fromname修改名称为toname。
ftp.storbinaly("STOR filename.txt",file_handel,bufsize) #上传目标文件
ftp.retrbinary("RETR filename.txt",file_handel,bufsize)#下载FTP文件

'''
