#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs

import datetime 
import locale   

from pywinauto import application
from pywinauto import tests
from pywinauto.findbestmatch import MatchError
from pywinauto import findwindows
from pywinauto import WindowAmbiguousError
from pywinauto.controls import WrapHandle


#日本語対応
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

#実行時間測定
startTime = datetime.datetime.today()
d=startTime

#talkの定義（talkの内容をtalkroidが再生）
talk=''
fin  = codecs.open('testText_utf-8.txt', 'r', 'utf-8')
for line in fin:
	talk=talk+line


#talkroidの起動
#addr='C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe'
#app = application.Application.start(addr)

#talkroidへの接続。接続に失敗した場合はtalkroid再起動
#talkroid実行ファイルのアドレス
addr='C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe'

app = application.Application()
try:
	app.connect_(path=addr)
except application.ProcessNotFoundError:
	app.start_(addr)

d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 

#talkroidの画面を取得
app_form = app.top_window_()

d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 

#文字を入力
app_form.TypeKeys('^A') 
app_form.TypeKeys(talk) 

#再生ボタンの押下
app_form_play = app_form['Button0']
app_form_play.Click()

#実行時間を表示
d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 
