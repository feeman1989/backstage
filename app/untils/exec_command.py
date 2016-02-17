# -*- coding: utf-8 -*-
import paramiko
def cmd_command(address,command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address,5637,"root", "LCjXhUzGf7b8NzWe")
        stdin,stdout,stderr = ssh.exec_command(command)
        out = stdout.readlines()
        ssh.close()
        return out
    except:
        return "Command Error!"


