#！ /usr/bin/env python
#! -*-coding:utf-8 -*-
#!Author:wuhao

import os
from  django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自吴浩的测试邮件',
        '欢迎访问吴浩的博客',
        'wuhao_i123@sina.com',
        ['1150238638@qq.com'],
    )