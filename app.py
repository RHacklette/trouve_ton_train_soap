import os

cmd="/app/.heroku/python/bin/ladon-3.8-ctl testserve SOAPServer.py -v -p 80"
os.system(cmd)
