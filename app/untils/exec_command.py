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
        print out
    except:
        print "Command Error!"
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a","--address",dest="address",default="localhost",help="ADDRESS FOR COMMAND!",metavar="ADDRESS")
    parser.add_option("-e","--command",dest="command",default="df",type="string",help="COMMAND FOR SERVER!",metavar="COMMAND")
    (options,args) = parser.parse_args()
    print 'options: %s, args: %s' % (options,args)
    cmd_command(options.address,options.command)
