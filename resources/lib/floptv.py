import sys
import urllib
import urllib2
import httplib
from xml.dom import minidom
from xml.parsers import expat

class FlopTV:
    def getShows(self):
        url = "http://www.floptv.tv/feeds/iphone/GetShows.ashx"
        xmldata = urllib2.urlopen(url).read()
        dom = minidom.parseString(xmldata)

        shows = []
        for showNode in dom.getElementsByTagName('show'):
            show = {}
            show["id"] = showNode.getElementsByTagName('id')[0].childNodes[0].data
            show["title"] = showNode.getElementsByTagName('titolo')[0].childNodes[0].data
            show["thumb"] = showNode.getElementsByTagName('thumb')[0].childNodes[0].data
            shows.append(show)
       
        return shows

    def getVideoByShow(self, showId):
        url = "http://www.floptv.tv/feeds/iphone/GetVideoByShow.ashx?id=%s" % showId
        xmldata = urllib2.urlopen(url).read()
        dom = minidom.parseString(xmldata)

        videos = []
        for videoNode in dom.getElementsByTagName('video'):
            video = {}
            videoId = videoNode.getElementsByTagName('id')[0].childNodes[0].data
            video["tvshowtitle"] = videoNode.getElementsByTagName('show')[0].childNodes[0].data
            video["title"] = videoNode.getElementsByTagName('titolo')[0].childNodes[0].data
            # description can be empty
            try:
                video["description"] = videoNode.getElementsByTagName('descrizione')[0].childNodes[0].data.strip()
            except IndexError:
               video["description"] = ""
            video["duration"] = videoNode.getElementsByTagName('durata')[0].childNodes[0].data
            # [TODO] pubdate missing
            video["thumb"] = self.getThumbURL(videoId)
            video["url"] = videoNode.getElementsByTagName('url3g')[0].childNodes[0].data
            videos.append(video)
            
        return videos

    def getThumbURL(self, videoId):
        #url = "http://floptv.cdn.crosscast-system.com/Images/%s/xl_thumbnail.jpeg" % videoId
        url = "http://floptv.cdn.crosscast-system.com/Images/%s/original_thumbnail.jpeg" % videoId
        return url

    def getPosterURL(self, videoId):
        # NB: Not all videos have a poster!
        url = "http://www.floptv.tv/feeds/iphone/img/video/%s.jpg" % videoId
        return url        
