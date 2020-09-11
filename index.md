# OctoPrint / OctoPi quality of life scripts

## screensaver management for TFT+TouchUI
here's how to turn the screensaver off when the printing starts and turn it back on when the printing is done.

1. grab the scripts from [screensaver folder here](https://github.com/HexNumbers/OctoPrint/tree/master/screensaver) and put them into the pi home folder
2. edit the OctoPrint's `config.yaml` - it hides under `~/.octoprint`, include the section below (you might need to change the paths to the scripts):

```events:
    enabled: true
    subscriptions:
    -   command: /home/pi/screensaver/startPrint.sh
        event: PrintStarted
        type: system
    -   command: /home/pi/screensaver/endPrint.sh
        event: PrintDone
        type: system
```
3. restart OctoPrint and enjoy your new screensaver behavior!
