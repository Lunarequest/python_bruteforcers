#!/bin/python3
import telnetlib
import os 
import argparse

def telconnect(host, username, password, port=23,code=0):
    tn =  telnetlib.Telnet(host)
    tn.read_until(b"login: ")
    tn.write(username.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii")+b"\n")
    out = tn.read_all(timeout=5)
    if "Connected" in out:
        code = 1
    return code
    tn.close()