import sublime, sublime_plugin, subprocess, os

PLUGIN_PATH = os.path.dirname(__file__)

class SaveListener(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		settings = view.window().settings()
		if settings.get('chrome_refresh_onsave_enabled', False):
			if settings.has('cr_url'):
				subprocess.call(['/usr/bin/osascript', PLUGIN_PATH+'/chromeopen.scpt', settings.get('cr_url')])
			else:
				subprocess.call(['/usr/bin/osascript', PLUGIN_PATH+'/chromerefresh.scpt'])

class ChromeRefreshCommand(sublime_plugin.ApplicationCommand):
	def __init__(self):
		self.path = os.path.dirname(__file__)

	def run(self):
		settings = sublime.active_window().settings()
		if settings.has('cr_url'):
			subprocess.Popen(['/usr/bin/osascript', PLUGIN_PATH+'/chromeopen.scpt', settings.get('cr_url')])
		else:
			subprocess.Popen(['/usr/bin/osascript', PLUGIN_PATH+'/chromerefresh.scpt'])

class ChromeRefreshEnableCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.settings().set('chrome_refresh_onsave_enabled', True)

class ChromeRefreshDisableCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.settings().set('chrome_refresh_onsave_enabled', False)

class ChromeRefreshSetUrlCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Associate url:", "http://localhost:8000/", self.on_done, None, None)
	def on_done(self, url):
		if url:
			self.window.settings().set('cr_url', url)
		else:
			self.window.settings().erase('cr_url')
