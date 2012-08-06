#coding=utf-8
def send_mail(to_list,sub,content):
    import smtplib
    from email.mime.text import MIMEText
#    to_list=['18766964456@139.com',]
    mail_host="smtp.163.com"  #设置服务器
    mail_user=""    #用户名
    mail_pass=""   #口令
    mail_postfix="163.com"  #发件箱的后缀
    
    me="groupmail"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

