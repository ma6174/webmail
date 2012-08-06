#!/usr/bin/env python
#coding=utf-8
import web
import urllib
import logging
from sendmail import send_mail
urls = (
    #    '/(.*)','hello',
    '/mailto/(.*)','webmail'
)

app = web.application(urls,globals())

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('webmail.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')  
fh.setFormatter(formatter)
logger.addHandler(fh)

class webmail:
    __doc__ ='''
    Send Mail to Anyone!
    usage:
    http://xxx.com/mailto/{mail_address}/{subject}/{body}
    example:
    http://xxx.com/mailto/aaaa@qq.com/subject/body/   
    multi-address:
    http://xxx.com/mailto/aaaa@qq.com/bbbb@163.com/subject/body/
    '''
    def GET(self,name):
        logger.info(name)
        info = urllib.unquote(name).split('/')
        info = [i for i in info if i != '']
        if len(info) < 3:
            return webmail.__doc__
        try:
            print ''
            send_mail(info[:-2],info[-2],info[-1])
        except:
            return 'Failed Send Mail'
        print info
        render = web.template.render('./')
        return render.pages(info[:-2],info[-2],info[-1])

if __name__=='__main__':
    app.run()

application = app.wsgifunc()
