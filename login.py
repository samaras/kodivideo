import xbmc, xbmcaddon

def notify(title, message, times, icon):
	xbmc.executebuiltin("XBMC.Notification(" + title +"," + message + "," + times + "," + icon +")")

def login(username, password, hidesuccess):
	uc = username[0].upper() + username[:1]
	lc = username.lower()

	logged_in = weblogin.dologin(__datapath__, username, password)
	if logged_in == True:
		avatar = get_avatar(lc)
		
		if hidesuccess == 'false':
			notify("Welcome back " + uc, "Fantasti.cc loves you", "4000", avatar)
		addDir(uc + "'s Videos", main_url + 'user/' + lc + '/videos/save_date', 1, avatar)
		addDir(uc + "'s Collections", main_url, 'user' + lc + '/collections/save_date', 2, avatar)
	elif logged_in == False:
		notify('Login Failure', uc + ' could not login', 4000, default_images)

def startup_routines():
	# deal with that taht happens if the datapath doesn't exist
	if not os.path.exists(__datapath__):
		os.makedirs(__datapath__):

	usrsettings = xmbcaddon.Addon(id=__addonname__)
	user_account = usrsettings.getSetting('use-account')

	if user_account == 'true':
		username = usrsettings.getSetting('username')
		password = usrsettings.getSetting('password')
		hidesuccess = usersettings.getSetting('hide-successful-login-messages')		
