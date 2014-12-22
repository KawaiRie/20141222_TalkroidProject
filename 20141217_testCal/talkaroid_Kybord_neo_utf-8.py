#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

import datetime 
import locale   


from pywinauto import application
from pywinauto import tests
from pywinauto.findbestmatch import MatchError
from pywinauto import findwindows
from pywinauto import WindowAmbiguousError
from pywinauto.controls import WrapHandle

startTime = datetime.datetime.today()
d=startTime

#Start talkroid 
#app = application.Application.start("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")

#Connect talkaroid
#If connection failed, talkroid restart

app = application.Application()
try:
	app.connect_(path="C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
except application.ProcessNotFoundError:
	app.start_("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")

d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 

#get talkroid window
app_form = app.top_window_()

d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 


app_form.TypeKeys('^A') 
talk=u'特徴の異なる2つのライブラリ「ギャラ子RED」「ギャラ子BLUE」を同梱。'
app_form.TypeKeys(talk) 

app_form_play = app_form['Button0']
app_form_play.Click()



d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 
