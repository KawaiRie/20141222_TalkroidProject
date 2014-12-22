from pywinauto import application
from pywinauto import tests
from pywinauto.findbestmatch import MatchError
from pywinauto import findwindows
from pywinauto import WindowAmbiguousError
from pywinauto.controls import WrapHandle

#Start talkroid 
#app = application.Application.start("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")

#Connect talkaroid
#if connection failed, talkroid restart
app = application.Application()
try:
	app.connect_(path="C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
except application.ProcessNotFoundError:
	app.start_("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
	

#get talkroid window
app_form = app.top_window_()

app_form.TypeKeys('%F') 
app_form.TypeKeys('^N') 

#send alt+F,ctrl+o to talkroid
app_form.TypeKeys('%F') 
app_form.TypeKeys('^O') 

app_file = app.top_window_()

app_file.TypeKeys('%N')
app_file.TypeKeys('testText_Unicode.txt')
app_file.TypeKeys('%O')

app_form_play = app_form['Button0']
app_form_play.Click()

#app_file_filename = app_file['ComboBoxEx']
#app_file.SetWindowText()

#app_file_Open = app_file['Btton0']
#app_file_Open.Click()

#app_file.print_control_identifiers()


#app_form_txtbox = app_form['WindowsForms10.RichEdit20W.app.0.33c0d9d']

#app_form_txtbox.Click()
#app_form_txtbox.SetFocus()
#morning = 'zzzz'
#app_form_txtbox.SetWindowText(morning)
#app_form_txtbox.SetWindowText(u'\u3053\u3093\u306b\u3061\u306f')
#print(app_form_txtbox.Texts())
#app_form.print_control_identifiers()