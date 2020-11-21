# Nightly Server Restart Script

## About
This script is for scheduling server restarts on 3D printers running Octoprint on a raspberry pi. It utilizes the OctoPrint API so it will not restart if a print is running or the printer is disconnected. It does attempt to recconnect once.

## Setup

1. Clone the script to your pi
```
git clone 
```

2. Navigate inside the folder
```
cd nightly_octopi_restart/
```

3. Fill in your API key and IP address into the config file.


4. Make the script executable 
```
chmod +x restart_print_check.py
```

5. Create/Edit your root user crontab

  1. Type `sudo crontab -e` and press enter.
  2. If this is your first time editing crontab, select option '1.' 
  3. Add `0 2 * * * /home/pi/nightly_octopi_restart/restart_print_check.py >> /home/pi/nightly_octopi_restart/restart_cron.log 2>&1` to the end of the file.
  4. Press CTRL S and then CTRL X.

## Troubleshooting

### Testing that your script can be run by crontab.
- Type into terminal `env -i /bin/bash --noprofile --norc` and press enter.
- Then type `/home/pi/nightly_octopi_restart/restart_print_check.py` and press enter.
- If the Pi restarts, your script has correct permissions and is in the correct location.
- If not, check the logs.