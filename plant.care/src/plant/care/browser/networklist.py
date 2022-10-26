# -*- coding: utf-8 -*-
import json
import time
import os
import re
import socket    
import multiprocessing
import subprocess
from Products.Five.browser import BrowserView

class NetworkView(BrowserView):
    def __call__(self, *args, **kwargs):
        self.my_ip = self.get_my_ip()
        self.show_ip = False
        self.error_msg = ''
        
        if 'start_scan' in self.request.form and self.request.method == 'POST':
            self.show_ip = True

        return super(NetworkView, self).__call__(*args, **kwargs)

    #---------------------------------------------------
    # return error msg string
    #---------------------------------------------------
    def get_errorMessage(self):
        return self.error_msg

    #---------------------------------------------------
    # return error msg string
    #---------------------------------------------------
    def get_my_ownip(self):
        return self.my_ip

    @property
    #---------------------------------------------------
    # return error msg string
    #---------------------------------------------------
    def check_showip(self):
        return self.show_ip

    #---------------------------------------------------
    # return error msg string
    #---------------------------------------------------
    def get_ip_list(self):
        lst = self.map_network()
        lst.sort()
        iptab = {}
        arpmap = self.get_arp_map()
        for ip in lst:
            if ip in arpmap:
                iptab[ip] = arpmap[ip]

        """
        for ip in lst:
            if ip==self.my_ip:
                continue
            if ip.endswith('.1'):
                continue
            iptab[ip] = self.gethostname(ip)
        """
        return iptab
    
    #---------------------------------------------------
    # return ip from client
    #---------------------------------------------------
    def get_my_ip(self):
        """
        Find my IP address
        :return:
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip


    def pinger(self,job_q, results_q):
        """
        Do Ping
        :param job_q:
        :param results_q:
        :return:
        """
        #DEVNULL = open(os.devnull, 'w')
        while True:
            ip = job_q.get()
            if ip is None:
                break
            try:
                subprocess.check_call(['ping', '-c', '1', '-q',ip],
                                    stdout=subprocess.PIPE)
                results_q.put(ip)
            except:
                pass
        time.sleep(2)


    def map_networkold(self,pool_size=255):
        """
        Maps the network
        :param pool_size: amount of parallel ping processes
        :return: list of valid ip addresses
        """
        def myping(host):
            response = os.system("ping -c 1 -q " + host)
            
            if response == 0:
                return True
            else:
                return False
        ip_list = list()

        # get my IP and compose a base like 192.168.1.xxx
        ip_parts = self.my_ip.split('.')
        base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

        # cue hte ping processes
        for i in range(1, 255):
            ip = base_ip + '{0}'.format(i)
            ret = myping(ip)
            if ret == True:
                ip_list.append(ip)
        return ip_list

    def map_network(self,pool_size=25):
        """
        Maps the network
        :param pool_size: amount of parallel ping processes
        :return: list of valid ip addresses
        """

        ip_list = list()

        # get my IP and compose a base like 192.168.1.xxx
        ip_parts = self.my_ip.split('.')
        base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

        # prepare the jobs queue
        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()

        pool = [multiprocessing.Process(target=self.pinger, args=(jobs, results)) for i in range(pool_size)]

        for p in pool:
            p.start()

        # cue hte ping processes
        for i in range(1, 255):
            jobs.put(base_ip + '{0}'.format(i))

        for p in pool:
            jobs.put(None)

        for p in pool:
            p.join()

        # collect he results,
        while not results.empty():
            ip = results.get()
            ip_list.append(ip)

        return ip_list

    def gethostname(self,ip):
        host_table = []
        retstr = ''
        process = subprocess.Popen(["host", ip],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                universal_newlines=True,close_fds=True)
        while True:
            output = process.stdout.readline()
            myout = output.strip()
            if len(myout)  > 5:
                retstr+=output
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                # Process has finished, read rest of the output 
                for output in process.stdout.readlines():
                    retstr+=output
                break
        process.stdout.close()
        tab = retstr.split('\n')
        for line in tab:
            if len(line)<2:
                continue
            s1 = line.find('pointer')
            if s1 > 0:
                zwline = line[s1+8:]
            else:
                s1 = line.find('in-addr.arpa')
                if s1 > 0:
                    zwline = line[s1+13:]
                else:
                    zwline = '??????'        
            host_table.append(zwline)
        return '<br>'.join(host_table)

    def get_arp_map(self):
        iptab = {}
        command = "arp -a"  # the shell command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
        #Launch the shell command:
        output = process.communicate()
        ostr = output[0].decode()
        linetab = ostr.split('\n')
        for ele in linetab:
            if ele:
                ele = ele.replace('\n','')
                if ele.startswith('PYBD'):
                    tab = ele.split(' ')
                    if '.' in tab[1]:
                        ipadr = tab[1].replace('(','')
                        ipadr = ipadr.replace(')','')
                    else:
                        continue
                    iptab[ipadr] = tab[0]
        return iptab          
