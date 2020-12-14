import MySQLdb
import MySQLdb.cursors
import settings
from flask import request


def db_connection():
    '''
    Database connections establishment.
    '''
    return (MySQLdb.connect(settings.HOST, settings.USER, settings.PASSWORD,
                            settings.DATABASE, cursorclass=MySQLdb.cursors.DictCursor,
                            charset="utf8"))
