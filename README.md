#TWITTER UTILS
================================================================================
Author: Minh-Hoang, Nguyen

Date  : 20/03/2012
================================================================================

##Dependencies
tweepy :   ```https://github.com/tweepy/tweepy```

Tkinter:   ```sudo apt-get install python python-tk idle python-pmw python-imaging``` in Debian

or ```yum install tkinter``` in Fedora Core 3
	
or see [http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter](http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter) for 
	   more details


##How to use:

```
$pwd
HUtweetutils
```

Create Database:
```
$mysqld &
$mysql -u root -p
type password
mysql> source twittersearch.sql
```
Run:
```
    python hugo/twitter/GUI.py to call interface and use!
```

##Features:

1. Search tweets and store in mysqldb
2. Post a message to own account


##License:

  All HUtweetutils-- source files are made available under the terms of the
  GNU Affero General Public License (AGPL).  See GNU-AGPL-3.0 files for
  details.


