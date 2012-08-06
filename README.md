<head><meta charset="UTF-8"></head>
#利用网页发送邮件
##原理：
    利用web.py模块接收一个http请求，请求中包含收信人，主题和邮件内容，   
然后分析这个请求，提取必要的信息，用smtp模块将邮件发送出去

##安装方法
* git clone git@github.com:ma6174/webmail.git
* 安装python-dev:   sudo apt-get install python-dev -y
* 安装uwsgi:        sudo easy_install uwsgi
* 安装web.py:       sudo easy_install web.py


##使用说明
首先打开sendmail.py,输入你的邮箱名和密码，    
运行./start.sh开始执行服务   
打开浏览器，输入“http://localhost:8080/mailto/”测试程序能否正常运行。   
在浏览器输入http://localhost:8080/mailto/XXXX@163.com/subject/body/测试能否正常发送邮件    
群发方法：在“mailto”和“subject”之间输入你要发送的邮箱即可，用“/”分隔开

