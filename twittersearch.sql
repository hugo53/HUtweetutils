DROP DATABASE IF EXISTS tweetsearch;

CREATE DATABASE tweetsearch;

USE tweetsearch;

CREATE TABLE tweet(
	tweet_id integer NOT NULL AUTO_INCREMENT,	
	username character varying(45),
	tweetcontent character varying(140),    
	PRIMARY KEY (tweet_id)
)DEFAULT CHARSET=utf8;
