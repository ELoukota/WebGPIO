# WebGPIO
A web UI for controlling the GPIO pins on a Raspberry Pi. (Forked from https://github.com/ThisIsQasim/WebGPIO)

Coded the layout to use CSS and apache2/php to dynamicly create the buttons and other features.
Added modules for Dallas Tempature sensors, and an MPU6050 as a leveling indicator.

To setup make sure you have:
Python3:
    python3-pip
    libpython3-dev
    (setuptools
    wheel
    flask
    pyyaml
    smbus2) in requirements.txt
 apache2:
    php:
        exif
        gd
        imagick

    

Clone the repo and create a config file named config.yml in the repo folder. Define pin numbers, in BCM format, grouped into "Zones" and "Appliances" in config.yml. See exampleconfig.yml for reference

    git clone https://github.com/ELoukota/WebGPIO
    cd WebGPIO
    sudo pip3 install -r requirements.txt (if you havent already installed the python3 requirements)
    cp exampleconfig.yml config.yml

Run with python

    python3 backend.py     

Access the UI at http://pi_ip_address:8000
