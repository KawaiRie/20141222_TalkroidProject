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

app_form.TypeKeys('%F') 
app_form.TypeKeys('^N') 


#send alt+F,ctrl+o to talkroid
app_form.TypeKeys('%F') 
app_form.TypeKeys('^O') 

app_file = app.top_window_()
d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 

app_file.TypeKeys('%N')

filename= 'testText_Unicode.txt'
app_file.TypeKeys(filename)
app_file.TypeKeys('%O')



app_form_play = app_form['Button0']
app_form_play.Click()



d = datetime.datetime.today()-startTime
print 'd == %s : %s\n' % (d, type(d)) 
