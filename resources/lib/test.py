from floptv import FlopTV

floptv = FlopTV()
#print floptv.getShows()
items = floptv.getVideoByShow("37")
for item in items:
    print item["tvshowtitle"]    
    print item["title"]
    print item["thumb"]
    print item["duration"]
    print item["description"]
    print item["rating"]
    print item["playcount"]
    print item["url"]
