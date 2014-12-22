from pywinauto import application
from pywinauto import tests
from pywinauto.findbestmatch import MatchError
from pywinauto import findwindows
from pywinauto import WindowAmbiguousError
from pywinauto.controls import WrapHandle

app = application.Application.start("c:\windows\system32\calc.exe")
#app = application.Application()
#try:
#	app.connect_(path="C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
#except application.ProcessNotFoundError:
#	app.start_("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
	

app_form = app.top_window_()
app_form_2 = app_form['2Button']
app_form_5 = app_form['5Button']
app_form_plus = app_form['+Button']
app_form_eq = app_form['=Button']

app_form_2.Click() 
app_form_plus.Click()
app_form_5.Click()
app_form_eq.Click()


#print(app_form)
#app_form_txtbox = app_form['WindowsForms10.RichEdit20W.app.0.33c0d9d1']
#print(app_form_txtbox)
#app_form_txtbox.Click()
#app_form_txtbox.SetFocus()
#app_form_txtbox.SetWindowText('vvv')
#print(app_form_txtbox.Texts())
#app_form.print_control_identifiers()