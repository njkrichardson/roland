test:
	rm -rf tmp tracking destination
	mkdir tmp tracking destination
	launchctl stop com.startup.test
	launchctl load ~/Library/LaunchAgents/com.startup.plist.test
	launchctl start com.startup.test
	pytest /Users/nickrichardson/Desktop/personal/projects/pyauto/test_auto_filehander.py
