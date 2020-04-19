# elanus 🏎️ 

elanus is a wifi fpv car powered by Raspberry Pi 🍓

![Demo](https://media.giphy.com/media/f6Q2r3odxQ3MU3kDp3/giphy.gif)

## Installation

### Connect the drive rand the motors according to the circuit below.
The gyro sensor can be ignored for the moment
![Circuit](https://raw.githubusercontent.com/xrv0/elanus/master/Elanus_circuit.jpg)

### Download the project and install dependencies

```bash
git clone https://github.com/xrv0/elanus.git
cd elanus
pip3 install -r requirements.txt
```

### Install motion to enable video streaming

```bash
sudo raspi-config
# Then go into Interface Options -> Camera and enable it

sudo apt-get install motion
sudo modprobe bcm2835-v4l2

sudo cp conf/motion /etc/default/motion
sudo cp conf/motion.conf /etc/motion/motion.conf

sudo service motion start
```

[Motion Installation Guide for more information](https://motion-project.github.io/motion_config.html#basic_setup_picam)

## Usage

Run the following command to start the frontend aswell as the backend

```bash
python3 main.py
```
Open your browser and navigate to http://raspberrypi.local:5000 or http://YOUR-PIs-IP-ADRESS:5000

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
