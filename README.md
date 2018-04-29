# Light controller #

## TL;DR ##

Light controller is a web app for controlling a light (or any plug-powered appliance) that is server from a Raspberry Pi. It uses a React client, a flask server and an Energenie Pi-Mote to control the plugs. It is intended as a bit of fun and maybe a learning tool for someone interested in full-stack development with a physical edge.

## Setting up ##

I performed this setup on an old Raspberry Pi Model B and an Ubuntu Linux dev machine. I cannot vouch for the instructions accuracy for newer Pis or different OSes. 

### The Raspberry Pi ###

A Raspberry Pi and a Pi-Mote starter kit https://energenie4u.co.uk/catalogue/product/ENER002-2PI are required. The manuel for the Pi-Mote can be found here https://energenie4u.co.uk/res/pdfs/ENER314%20UM.pdf. The code to control the plugs is in server/live_controller and is somewhat taken from the manuel. You should first read the manuel and run the code in it to set up the Pi-Mote.

### The Web App ###

I suggest for development you use a separate machine to the Pi. First install Node.js (https://nodejs.org/en/download/). Then install Python3 (https://www.python.org/downloads/). To control your Python dependencies, I advise you use a virtual environment. To set this up run (sudo if necessary): 
``` 
pip install virtualenv
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -p python3 light
```
Ensure you are in the virtualenv by checking that "(light)" now appears before the prompt in your shell. You should then install the Python requirements for the project into the virtualenv:
```
pip install -r requirements.txt
```
Install the Javascript client dependencies.
```
npm i --prefix client
```

You can now launch the dev version of the app from the root of the repo with:
```
./manage.sh run_dev
```
The dev client will be on http://localhost:3000.

You can also build launch the live version of the app with:
```
./manage.sh build_client
./manage.sh run_live_without_pimote
```
The live client will be on http://localhost:5678.

### Deploying to the Raspberry Pi

I like to work with a headless Pi and control it remotely from my development machine using ssh and sftp. To put the code on the Pi, start and sftp session and do:
```
mkdir light_controller
cd light_controller
put -r server
put -r client/build
put live_main.py
put manage.sh
put requirements.txt
```
Note that we do not just put the full repo on the Pi as the node_modules are unnecessary but large (welcome to modern front-end development).

Then start and ssh session and ensure that Python3 is installed on the Pi. Then set up the virtual environment as you did for the development machine. You will need to add the python3 Raspberry Pi GPIO library:
```
sudo apt-get -y install python3-rpi.gpio
pip install RPi.GPIO
```
You can now get the Pi-Mote ready on the Pi and your light, and run:
```
./manage.sh run_live_with_pimote
```
The live client will be on http://localhost:5678. You should now be able to control the light with the client. This page will be accessible from anywhere in your local network with http://$PI_HOSTNAME:5678.

### Global Routing ###

To make your light controllable from anywhere in the world, you will need to log into your router and make a forwarding rule from port 80 to port 5678 on your Raspberry Pi. You should now be able to control the light outside your local network with http://$YOUR_ROUTER'S_GLOBAL_IP_ADDRESS. It is likely that you have Dynamic DNS, so $YOUR_ROUTER'S_GLOBAL_IP_ADDRESS will not be fixed. To deal with this, you can use a free Dynamic DNS service like https://www.noip.com/. You can then add a CNAME record to a domain you own that routes to the hostname provided by noip to make your light controllable from your own domain.

### Acknowledgements ###
* create-react-scripts was used for the client.
* The plug_interface.py code is a modified version of the code from https://energenie4u.co.uk/res/pdfs/ENER314%20UM.pdf.
* https://openclipart.org/ and https://www.iconfinder.com/ were used for images.