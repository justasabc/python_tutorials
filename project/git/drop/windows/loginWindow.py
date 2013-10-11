import pygtk
pygtk.require("2.0")
import gtk
import sys
import hashlib 

class LoginWindow:
	"""
	signals
	loginWindow: destroy --- destroy_handler
	loginImage
	txtEmail
	txtPassword
	lblMessage
	btnSignIn: clicked --- sign_in_handler
	btnCancel: clicked --- destroy_handler
	btnFogotPassword
	"""
	def __init__(self,app):
		self.app = app
		self.app_icon = "./windows/resource/icon/dewdrop-128-black.png"
		self.image = "./windows/resource/icon/dewdrop-128-black.png"
		self.glade = "./windows/data/ui/loginWindow.glade"

		self.builder = gtk.Builder()
		self.builder.add_from_file(self.glade)
		self.builder.connect_signals(self)
		self.win = self.builder.get_object('loginWindow')
		self.win.set_icon_from_file(self.app_icon)
		self.builder.get_object('loginImage').set_from_file(self.image)
		# connect events
		self.win.connect('destroy',self.close)
		self.builder.get_object('btnSignIn').connect('clicked',self.sign_in)
		self.builder.get_object('btnCancel').connect('clicked',self.close)
		self.win.show_all()
	
	def show(self):
		gtk.main()

	def close(self,widget,data=None):
		print('loginWindow is going to close...')
		gtk.main_quit()

	def sign_in(self,widget,data=None):
		print('login ...')
		email = self.builder.get_object('txtEmail').get_text()
		password = self.builder.get_object('txtPassword').get_text()

		if not email or not password:
			self.builder.get_object('lblMessage').set_text("Please fill out both fields")
			return False

		passhash = hashlib.sha1(password).hexdigest()
		del password
		rtn = self.app.test_credentials(email, passhash)
		if rtn == True:
			self.app._cfg.set('email', email)
			self.app._cfg.set('passhash', passhash)
			self.app._cfg.save()
			# close loginWindow
			self.builder.get_object('loginWindow').destroy()
			self.app.login()
		else:
			self.builder.get_object('lblMessage').set_text(rtn.get_message())
		return True

