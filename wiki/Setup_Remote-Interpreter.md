In PyCharm it is possible to run your program on a remote interpreter instead of your local system.
This is useful if you have a server where your necessary environment is already set up.
This is the case for us, because on the lsdf cluster, we have a working Ginkgo and SSGet installation.

## Necessary steps

### In PyCharm

* open PyCharm
* go to `Tools` &rarr; `Deployment`  &rarr; `Configuration`
* type `SFTP`
* host: `lsdf-28-131.scc.kit.edu`
* port: `22`
* your username: `u****`
* authentication: `your password`
* root path: `autodetect`
* `Done`

Next:

* go to `File` &rarr; `Setting` &rarr; `Project` &rarr; `Project Interpreter`
* click the wheel and selet `Add` 
* select `ssh interpreter`
* select `existing server config`
* select the server you just created in the previous steps
* choose `create copy`
* choose interpreter `/usr/bin/python3.6`
* leave settings for `sync folder`
* check the box next to `autmatically upload`

Now you are done setting up PyCharm and it should start a process that uploads your project to the server.

### On the server

The last thing to do is installing all dependencies on the server.
You most likely won't have root access and therefore need a workaround to install packages.

* open a terminal and ssh into the server.
* look for the folder `tmp`.

In this folder should be a folder called `python_project_` followed by same number.
This is where your project is uploaded to.

* open this folder 
* enter the command

> wget https://bootstrap.pypa.io/get-pip.py && python3.6 -m get-pip.py --user
> python3.6 -m pip install -r requirements.txt --user

This will allow you install all necessary dependencies without having root access on the server.

