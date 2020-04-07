import os

cmd="/app/.heroku/python/bin/ladon-3.8-ctl testserve SOAPServer.py -v -p 8080"
os.system(cmd)
