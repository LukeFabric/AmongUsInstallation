"""
Automates the reinstallation of Among Us
"""

import subprocess
import pyautogui, time, os

def runPowershell(script):
    POWERSHELL_PATH = 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\powershell.exe'
    commandline_options = [POWERSHELL_PATH, script]
    process_result = subprocess.run(commandline_options, universal_newlines = True)
    print(process_result.returncode)
def main():
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.alert(text='Don\'t touch your keyboard or mouse.', title='', button='OK') 
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    runPowershell(os.getcwd() + '\\resources\\fixBlackScreen.ps1')
    #'C:\\AmongUsInstallation\\src\\amongussteamscript\\resources\\fixBlackScreen.ps1'
    pyautogui.keyDown("win")
    pyautogui.press("up")
    pyautogui.keyUp("win")
    pyautogui.click(x=217, y=67)
    time.sleep(1)
    pyautogui.click(x=222,y=306)
    time.sleep(1)
    pyautogui.click(button='right',x=222,y=306)
    time.sleep(1)
    pyautogui.moveTo(346,459)
    time.sleep(1)
    pyautogui.click(x=482,y=628)
    time.sleep(1)
    pyautogui.click(x=1085, y=602)
    time.sleep(1)
    pyautogui.click(x=499, y=534)
    time.sleep(1)
    pyautogui.click(x=865, y=735)
    time.sleep(30)
    runPowershell(os.getcwd() + '\\resources\\moveManifest.ps1')
