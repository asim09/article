Article App
============

Author Can Add their Articles with multiple tags.

##To Install system follow these steps

# Create custom virtual environment for your project



# Install python "virtaulenv" on ubuntu
# Activate the "virtaulenv"
$ souurce env/bin/activate   #assunimg env is virtaulenv's name

# Install Flask Framework
$ pip install flask

# Install MySQL server
$ sudo apt-get install mysql-server
$ sudo apt-get install libmysqlclient-dev

# cd to "pyenv" directory
$ cd pyenv

# Create python "virtaulenv"
$ virtualenv env --no-site-packages

# Activate python virtualenv
$ source eve/bin/activate

# To check the python location
$ which python

# Install all the required packages
$ pip install -r ../requirement.txt

# Create mysql database named as "article_database"
CREATE DATABASE article_database

# Create two table article:
$ CREATE TABLE `article` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL DEFAULT '',
  `description` text,
  `author` varchar(255) DEFAULT NULL,
  `soft_delete` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

# Create two table tags:

CREATE TABLE `tags` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tag` varchar(11) NOT NULL DEFAULT '',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

# To run the Server:
$ python app.py

# Project structure is in zip file for the reference.



# Todo things (after login with Super User)


