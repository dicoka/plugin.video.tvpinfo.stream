# -*- coding: UTF-8 -*-
import sys, os
import urllib, urlparse, urllib2, re
import xbmcgui, xbmc, xbmcaddon, xbmcplugin

def readPage(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',
                   ' Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    return page


page = readPage('http://tvpstream.tvp.pl')
match = re.compile('src=\"(/sess/tvplayer.php.+?)\"',re.DOTALL).findall(page)
page = readPage('http://tvpstream.tvp.pl'+match[0])
match2 = re.compile('src.+(http.+?tvpinfo.m3u8)',re.DOTALL).findall(page)
listitem = xbmcgui.ListItem('TVP.INFO Stream')
listitem.setInfo('video', {'Title': 'TVP.INFO Stream'})
addon = xbmcaddon.Addon('plugin.video.tvpinfo.stream')
listitem.setArt({'thumb': os.path.join(addon.getAddonInfo('path'), "icon.png")})
xbmc.Player().play(match2[0], listitem)
