from pywinauto import application
from pywinauto import tests
from pywinauto.findbestmatch import MatchError
from pywinauto import findwindows
from pywinauto import WindowAmbiguousError
from pywinauto.controls import WrapHandle

#app = application.Application.start("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
app = application.Application()
try:
	app.connect_(path="C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
except application.ProcessNotFoundError:
	app.start_("C:\Program Files\YAMAHA\galacoTalk\galacoTalk.exe")
	

app_form = app.top_window_()
app_form_play = app_form['Button0']
app_form_play.Click()


#print(app_form)
#print(app_form_txtbox)
#app_form.print_control_identifiers()