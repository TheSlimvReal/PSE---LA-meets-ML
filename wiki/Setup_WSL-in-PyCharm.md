For some of our modules, it's necessary to run them on linux or macOs. 
If you still want to work on windows, there is a pretty easy way to set up a linux interpreter in PyCharm.
This will result in you code running on a ubuntu subsystem on your windows.

## Installing Linux subsytem, configuring it for PyCharm
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

## Install SSGet

SSGet is one tool used in the collector that needs a linux environment.
Installing SSGet is very easy in the linux subsystem.
Open the ubuntu bash and enter:

```
git clone https://github.com/ginkgo-project/ssget.git
cd ssget
sudo make install

```
