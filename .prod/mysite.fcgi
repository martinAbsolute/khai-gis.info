#!/home/httpd/vhosts/martinb.mcdir.ru/private/venvs/myvenv/bin/python
import sys, os

sys.path.append('/home/httpd/vhosts/martinb.mcdir.ru/private/venvs/myvenv/lib/python3.4/site-packages')
sys.path.append('/home/httpd/vhosts/martinb.mcdir.ru/private/venvs/myvenv/lib64/python3.4/site-packages')
sys.path.append("/home/httpd/vhosts/martinb.mcdir.ru/private/app/myapp")

os.environ['DJANGO_SETTINGS_MODULE'] = "myapp.settings"

from django_fastcgi.servers.fastcgi import runfastcgi
from django.core.servers.basehttp import get_internal_wsgi_application

wsgi_application = get_internal_wsgi_application()
runfastcgi(wsgi_application, method="threaded", daemonize="false")
