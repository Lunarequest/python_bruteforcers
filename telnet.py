#!/bin/python3
import telnetlib
import os 
import argparse

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
def succes()
def bruteforcer(host, passwordlist, username, port=None):
    check = os.path.isfile(passwordlist)
    if check:
        check = os.path.isfile(username)
        if check:
            pass
        else:
            with open(passwordlist,'r') as passwords:
                for password in passwords:
                    code = telconnect(host,username,password)
                    if code == 0:
                        succes(username, password)
                        break
    else:
        print("passwordlist is not valid path")
        exit()