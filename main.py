import subprocess
import sys
import logging
import os
from pynput.keyboard import Listener

gameproc = ["SunloginClient","ToDesk_Service","SunloginClient Networking","SunloginClient_Helper","SunloginClient_Desktop"]

def run(key):
    all_key.append(str(key))
    if 'Key.shift_r' and 'Key.alt_r' in all_key:
        all_key.clear()

        for process in gameproc:
            cmd = "ps aux| grep '%s'|grep -v xyj " % process
            out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            infos = out.stdout.read().splitlines()

            for i in infos:
                pid = i.split()[1]
                pid_1 = str(pid,'utf-8')
                cmd = 'sudo kill -9 ' + str(pid_1)
                print(cmd)
                subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)

        print('over')

if __name__ == '__main__':
    all_key = []
    with Listener(on_press=None, on_release=run) as listener:
        listener.join()
