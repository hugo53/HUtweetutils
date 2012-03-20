'''
Created on Mar 20, 2012

@author: root
'''

import urllib2
import MySQLdb as mdb
import MySQLdb
import sys
import json



def search(query):
    url = 'http://search.twitter.com/search.json?q='
    url +=query
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def jsonParser(jsonString):
    data = json.loads(jsonString)
    rst = data['results']   #    >>> rst is list (list of result)
    
    listTweets = []
    for i in rst:           #    >>> i is dict
        tweet = {i['from_user']:i['text']}
        listTweets.append(tweet) #>>> i['text'] will get value of key 'text'
    
    return listTweets

def insertMySQL(tweetDict):
    con = None
    try:
        con = mdb.connect('localhost', 'root', 'sa', 'tweetsearch');
        cur = con.cursor()
        with con:
            cur = con.cursor()
            checkquery = "SELECT * FROM tweet WHERE username = '" \
                            + MySQLdb.escape_string(tweetDict.keys()[0]) \
                            + "' AND tweetcontent = '" \
                            + MySQLdb.escape_string(tweetDict.get(tweetDict.keys()[0])) \
                            +"'"
            cur.execute(checkquery)
            rows = cur.fetchall()
            if(len(rows) == 0):
                query = "INSERT INTO tweet(username, tweetcontent) VALUES('" \
                        + MySQLdb.escape_string(tweetDict.keys()[0]) \
                        + "', '" \
                        + MySQLdb.escape_string(tweetDict.get(tweetDict.keys()[0])) \
                        + "')"
                cur.execute(query)
                return True
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()
    return False

if __name__ == '__main__':
    pass