#!/usr/bin/env pyhton
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# 设置邮箱的域名
HOST = 'smtp.qq.com'
# 设置邮件标题
SUBJECT = '111111'
# 设置发件人邮箱
FROM = '1316367833@qq.com'
# 设置收件人邮箱
TO = '473359330@qq.com'
message = MIMEMultipart('related')
 
#--------------------------------------发送文本-----------------
# 发送邮件主体到对方的邮箱中
message_html = MIMEText('<h2 style="color:red;font-size:100px">111111</h2><img src="cid:big">','html','utf-8')
message.attach(message_html)
 
# 设置邮件发件人
message['From'] = FROM
# 设置邮件收件人
message['To'] = TO
# 设置邮件标题
message['Subject'] = SUBJECT
 
# 获取简单邮件传输协议的证书smtplib.SMTP_SSL(host='smtp.gmail.com').connect(host='smtp.gmail.com', port=465)
email_client = smtplib.SMTP_SSL(host='smtp.qq.com')
# 设置发件人邮箱的域名和端口，端口为465
email_client.connect(host='smtp.qq.com', port=465)
# ---------------------------邮箱授权码------------------------------
result = email_client.login(FROM,'acnfxageoiidgijd')
print('登录结果',result)
email_client.sendmail(from_addr=FROM,to_addrs=TO.split(','),msg=message.as_string())
# 关闭邮件发送客户端
email_client.close()
