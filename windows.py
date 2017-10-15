import pyautogui as auto

print("moving chrome....")
chrome = auto.getWindow('Google Chrome')
if chrome != None:
	chrome.restore()
	chrome.move(-1920, 0)
	chrome.maximize()

print("moving Skype....")
skype = auto.getWindow('Skype')
if skype != None:
	skype.restore()
	skype.move(2873, 515)
	skype.resize(980, 495)

print("moving Slack....")
slack = auto.getWindow('Slack')
if slack != None:
	slack.restore()
	slack.move(2880, 0)
	slack.resize(960, 520)

print("moving Powershell....")
powershell = auto.getWindow('Windows Powershell')
if powershell != None:
	powershell.restore()
	powershell.move(2880, 0)
	powershell.resize(960, 515)

print("moving Visual Studio Code....")
vsCode = auto.getWindow('Visual Studio Code')
if vsCode != None:
	vsCode.move(-8, -8)
	vsCode.maximize()

print("moving Visual Studio....")
vs= auto.getWindow('Microsoft Visual Studio')
if vs!= None:
	vs.move(0, 0)
	vs.maximize()

print("moving Android Studio ....")
AndroidStudio = auto.getWindow('Android Studio')
if AndroidStudio != None:
	AndroidStudio.move(-8, -8)
	AndroidStudio.maximize()

print("moving Gogland....")
gogland = auto.getWindow('Gogland')
if gogland != None:
	gogland.move(-8, -8)
	gogland.maximize()