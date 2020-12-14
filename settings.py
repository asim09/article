import os

# Database credential can be defined here for Staging and production server
current_dir = os.getcwd()
if 'development' in current_dir:

    HOST           = "127.0.0.1"
    USER           = "root"
    PASSWORD       = "root"
    DATABASE       = "article_database"
    SECRET_KEY     = "bruce wayne is the mask"



