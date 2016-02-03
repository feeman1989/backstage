# -*- coding: utf-8 -*-
import paramiko
from optparse import OptionParser
def cmd_command(address,command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address,5637,"root", "123")
        stdin,stdout,stderr = ssh.exec_command(command)
        out = stdout.readlines()
        ssh.close()
        return out
    except:
        return "Command Error!"
    parser = OptionParser()
    parser.add_option("-a","--address",dest="address",default="localhost",help="ADDRESS FOR COMMAND!",metavar="ADDRESS")
    parser.add_option("-e","--command",dest="command",default="df",type="string",help="COMMAND FOR SERVER!",metavar="COMMAND")
    (options,args) = parser.parse_args()
    print 'options: %s, args: %s' % (options,args)
cmd_command(options.address,options.command)
