import pygtk
pygtk.require("2.0")
import gtk

class App:
	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file('hello.glade')
		builder.connect_signals(self)
		win = builder.get_object('window1')
		win.show_all()

	def on_window1_destroy(self,data):
		print('program is going to exit...')
		gtk.main_quit(data)

def main():
	App()	
	gtk.main()

if __name__ == "__main__":
	main()
