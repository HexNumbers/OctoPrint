# screensaver management for TFT+TouchUI
here's how to turn the screensaver off when the printing starts and turn it back on when the printing is done  
  
1. grab the scripts from [screensaver folder here](https://github.com/HexNumbers/OctoPrint/tree/master/screensaver) and put them into the pi home folder, say under `/home/pi/screensaver`
2. edit the OctoPrint's `config.yaml` - it hides under `~/.octoprint`, include the section below:
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
  
  
[{BACK}](https://hexnumbers.github.io/OctoPrint/)
