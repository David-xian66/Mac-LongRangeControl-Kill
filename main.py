import subprocess
import sys
import logging
import os
from pynput.keyboard import Listener

gameproc = ["SunloginClient","ToDesk_Service","SunloginClient Networking","SunloginClient_Helper","SunloginClient_Desktop"]

def on_press(key):
    pass

def getPid(process):
    cmd = "ps aux| grep '%s'|grep -v xyj " % process
    # cmd = "ps aux| grep '%s'" % process
    print(cmd)
    logging.info(cmd)
    out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    infos = out.stdout.read().splitlines()
    print(cmd)
    print('============')
    print(infos)
    pidlist = []
    """
    if len(infos) >= 1:
        for i in infos:
            pid = i.split()[1]
            if pid not in pidlist:
                pidlist.append(pid)
        return pidlist
    else:
        return -1
    """
    for i in infos:
            pid = i.split()[1]
            pidlist.append(pid)

    return pidlist

def run(key):
    all_key.append(str(key))
    #print('===快捷键===')
    #print(key)
    #print('===========')
    if 'Key.shift_r' and 'Key.alt_r' in all_key:
        all_key.clear()
        print('-----运行-----')
        pid = []
        for process in gameproc:
            pid1 = getPid(process)
            print(pid)
            for pid_1 in pid1:
                pid.append(pid_1)

        print('kill进程\n========')
        print(pid)
        for pid_1 in pid:

            pid_2 = str(pid_1).split("b'")[1]
            pid_3 = str(pid_1).split("'")[1]
            cmd = 'sudo kill -9 ' + str(pid_3)
            print(cmd)
            out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print(out.stdout.read().splitlines())
        print('-----完成-----')



def start_listen():
    with Listener(on_press=None, on_release=run) as listener:
        listener.join()


if __name__ == '__main__':
    all_key = []
    start_listen()