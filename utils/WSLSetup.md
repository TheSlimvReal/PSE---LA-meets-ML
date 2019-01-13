## Manual for Installing Linux Subsystem, configuring it for PyCharm and installing ssget
* Install Ubuntu from the Microsoft Store
* After installing, open your linux bash and type:

```
sudo apt-get update
sudo apt-get install build-essential
```

* Now install python3.6:

```
sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip
```

* Now Open Pycharm Professional
* go to File -> Settings -> Project: <Projectname> -> Project Interpreter -> click to gear next to the Project Interpreter: box -> choose "add"
-> choose "WSL" on the left hand side -> Linux Distribution "Ubuntu",
* Python interpreter path "/usr/bin/python3.6" -> click ok
* now pycharm displays missing requirements: click "Install requirements"

* At the end you can install ssget:

```
git clone https://github.com/ginkgo-project/ssget.git
cd ssget
sudo make install

```
