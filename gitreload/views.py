from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
import os
@csrf_exempt
def home(request):
    if request.method == 'POST':
        print 'ref is', request.POST.get('ref')
        os.chdir("/home/django/getftw/getftw/getftw")
        os.system("git pull")
        os.chdir("/home/django/getftw/env/bin")
        os.system("supervisorctl -c supervisor.conf < /home/django/gitreload/gitreload/supervisorctl_commands.txt")
        return HttpResponse(simplejson.dumps({'status' : 'success'}), content_type="application/json; charset=utf-8")
    else:
        return HttpResponse(simplejson.dumps({'status' : 'failure'}), content_type="application/json; charset=utf-8")
