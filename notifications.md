# notifications through SMS for OctoPrint
here's how to receive the sms notification when the print is complete (with the picture of your thingy!)  
  
1. register an email account, anything will do, my example uses gmail
2. for gmail, enable "less secure apps authorization" here -> https://myaccount.google.com/lesssecureapps
note: make sure you are doing it for the new account you created at step 1
3. grab the scripts from [notifications folder here](https://github.com/HexNumbers/OctoPrint/tree/master/notifications) and put them into the pi home folder, say under `/home/pi/notifications`
4. edit the script:
	* GMAIL_USERNAME and GMAIL_PASS are pretty self-explanatory 
	* RECEPIENT is where all the magic happens, US carriers offer the email to sms gateways that the script is using for T-Mobile it's <your number>@tmomail.net. here's a short list for other carriers:
		- AT&T: @mms.att.net
		- Verizon: @vtext.com
		- Sprint: @page.nextel.com
	    if your carrier is not listed - you'll have to do your own research. if your carrier doesn't provide this service, you'll have to create your own script using some other means, sorry ¯\\_(ツ)_/¯
	* SNAP_URL is the URL your mjpg-streamer or what have you is using for snapshots, the same that is configured in OctoPrint
	* MESSAGE is self-explanatory too
	* ROTATE_IMAGE - my webcam is upside down, the general consensus is that it's easier to use tricks like CSS image rotation than make mjpg-streamer rotate the stream for a non-pi USB cam. if you set this to true, the script will rotate the snapshot 180 degrees.
5. make OctoPrint execute the script when the print is complete:
	- Option A: edit the OctoPrint's `config.yaml` - it hides under `~/.octoprint`, include the section below:
		```events:
			enabled: true
			subscriptions:
			-   command: python /home/pi/notifications/sms.py
				event: PrintDone
				type: system
		```
	- Option B: if you are using the [screensaver scripts](https://hexnumbers.github.io/OctoPrint/screensaver), just add `python /home/pi/notifications/sms.py &` to your endPrint.sh
6. restart OctoPrint, add a contact with a cute picture for your printer's email for some additional personality, enjoy getting the messages when the print is done
  
  
[{BACK}](https://hexnumbers.github.io/OctoPrint/)
