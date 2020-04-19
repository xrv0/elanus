import subprocess


def get_signal_strength():
    cmd = subprocess.Popen('/sbin/iwconfig wlan0', shell=True,
                           stdout=subprocess.PIPE)
    for line in cmd.stdout:
        if 'Link Quality' in line:
            print(line.lstrip(' '))
        elif 'Not-Associated' in line:
            print('No signal')
