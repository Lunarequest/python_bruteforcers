#!/bin/python3
import telnetlib
import os 
import argparse

def telconnect(host, username, password, port=23):
    tn =  telnetlib.Telnet(host)
    tn.read_until(b"login: ")
    tn.write(username.encode("ascii")+b"\n")
    tn.read_until(b"Password: ")