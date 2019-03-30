# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from django.contrib import auth
from models import Machine_Info
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context
from app.untils.exec_command import cmd_command
from app.untils.alter_openserver_time import alter_open_server

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

@login_required
def machine_info(request):
    if request.method == "GET":
        machine_infos = Machine_Info.objects.order_by('-id')
        return render_to_response("machine_info.html",{'machine_infos':machine_infos})
@login_required
def alter_open_server_time(request):
    if request.method == "GET":
        server_infos = Machine_Info.objects.order_by('-id')
        return render_to_response("alter_open_server_time.html",{'server_infos':server_infos})
    elif request.method == "POST":
        server_time = request.POST.get("server_time").split("-")
        server_time.reverse()
        server_time = "-".join(server_time)
        ip_list = request.POST.getlist("servers")
        ip_list = map(lambda x:x.split()[1],ip_list)
        alter_time = """sed -i "s/server_born_time =.*/server_born_time = %s 10:00/" server_bin/ws/ws.cfg""" % server_time.strip()
        restart = """cd server_bin;sh start.sh"""
        hosts = []
        results = []
        for host in ip_list:
            alter_open_server(host,alter_time)
            result2 = alter_open_server(host,restart)
            results.append(result2)
            hosts.append(host)
        return render_to_response("inbox.html")

@login_required
def exec_sys_command(request):
    if request.method == "GET":
        server_infos = Machine_Info.objects.order_by('-id')
        return render_to_response("exec_sys_command.html",{'server_infos':server_infos})
    elif request.method == "POST":
        sys_command = request.POST.get('sys_command')
        ip_list = request.POST.getlist('servers')
        ip_list = map(lambda x:x.split()[1],ip_list)
        results = []
        hosts = []
        for host in ip_list:
            result = cmd_command(host,sys_command)
            results.append(result)
            hosts.append(host)
        adict = dict(zip(hosts,results))
        return render_to_response("inbox.html",{"results":adict})

@login_required
def open_server(request):
    if request.method == "GET":
        server_infos = Machine_Info.objects.order_by('-id')
        return render_to_response("open_server.html",{'server_infos':server_infos})

@login_required
def upload_file(request):
    if request.method == "GET":
        server_infos = Machine_Info.objects.order_by('-id')
        return render_to_response("uploadfile.html",{"server_infos":server_infos})
    elif request.method == "POST":
        filename = request.FILES.get("uploadfile")
        f = open("upload/%s"%filename,"w")
        for i in filename.chunks():
            f.write(i)
        f.close()
		print 'test app page'
        return render_to_response("inbox.html")



