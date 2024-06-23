"""
Automates the reinstallation of Among Us
"""

import subprocess
import pyautogui, time

def runPowershell(script):
    POWERSHELL_PATH = "C:\system32\WindowsPowershell\v5.1\powershell.exe"
    commandline_options = [POWERSHELL_PATH, script]
    process_result = subprocess.run(stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
    print(process_result.returncode)
def main():
    screenWidth, screenHeight = pyautogui.size()
    
    pyautogui.click(x=197, y=58)
    time.sleep(1)
    pyautogui.click(x=100,y=250)
    time.sleep(1)
    pyautogui.click(button='right',x=100,y=250)
    time.sleep(1)
    pyautogui.moveTo(230,365)
    time.sleep(1)
    pyautogui.click(x=349,y=493)
    time.sleep(1)
    pyautogui.click(x=1057, y=583)
    time.sleep(1)
    pyautogui.click(x=395, y=425)
    time.sleep(1)
    pyautogui.click(x=902, y=699)
