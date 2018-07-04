import sys 
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon


base_url = sys.argv[0]
addon_handle = int(sys.argv[1])

__addon__ = xbmcaddon.Addon(id='plugin.video.obrerostudio')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')


xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
	return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)


url = 'http://localhost:8081/2 - 2 - Quick Find (1018).mp4'
li = xbmcgui.ListItem('Quick Find 2.2', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
