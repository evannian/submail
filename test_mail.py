#coding=utf-8
from mysubmail.mail import Mail
from mysubmail import TextField, UrlField

class TestMail(Mail):
    name=TextField()
    active_url=UrlField()

mail = TestMail(name='jelly', active_url="http://www.baidu.com")
mail.send()


