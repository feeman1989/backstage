from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from models import Machine_Info
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context
import json
# Create your views here.
def login(request):
    if request.user is not None:
        logout(request)
    t = get_template("login.html")
    html = t.render(Context())
    return HttpResponse(html)
def account_auth(request):
    error = "username or password error!"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect("/index")
        else:
            return render_to_response("login.html",{"error":error})
@login_required
def index(request):
    return render_to_response("index.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")
def machine_info(request):
    if request.method == "GET":
        machine_infos = Machine_Info.objects.order_by('-id')
        return render_to_response("tables.html",{'machine_infos':machine_infos})

def open_server_time(request):
    return render_to_response("open_server_time.html")