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
#app_form.MenuSelect(u"(&F)->(&o)")

app_form_txtbox = app_form['WindowsForms10.RichEdit20W.app.0.33c0d9d']

#app_form_txtbox.Click()
#app_form_txtbox.SetFocus()
app_form_txtbox.SetWindowText('おはよう')
app_form_txtbox.SetWindowText(u'\u3053\u3093\u306b\u3061\u306f')
print(app_form_txtbox.Texts())
#app_form.print_control_identifiers()