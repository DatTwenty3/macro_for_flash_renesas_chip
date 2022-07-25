import pyautogui
import os
import time
import pyperclip
import psutil
# import wmi

delay = 0.2
counter_for_task_kill = 5
counter_for_flash = 5
clear_screen = lambda: os.system('cls')

def close_rtt_viewer():
    #Close log when it running
    global counter_for_task_kill
    while "JLinkRTTViewer.exe" in (p.name() for p in psutil.process_iter()):
        os.system("taskkill /im JLinkRTTViewer.exe")
        counter_for_task_kill = counter_for_task_kill - 1
        if (counter_for_task_kill == 0):
            break
    
def close_flash_programer():
    #Close flash when it running
    global counter_for_flash
    while "JFlashLite.exe" in (p.name() for p in psutil.process_iter()):
        os.system("taskkill /im JFlashLite.exe")
        counter_for_flash = counter_for_flash - 1
        if (counter_for_flash == 0):
            break

def print_logo():
    print('''
██╗░░░░░███████╗██████╗░░█████╗░████████╗
██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
██║░░░░░█████╗░░██║░░██║███████║░░░██║░░░
██║░░░░░██╔══╝░░██║░░██║██╔══██║░░░██║░░░
███████╗███████╗██████╔╝██║░░██║░░░██║░░░
╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░

▒█▀▄▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀█  ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀█  ▒█▀▀▀ ▒█░░░ ░█▀▀█ ▒█▀▀▀█ ▒█░▒█ 
▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█▄▄▀ ▒█░░▒█  ▒█▀▀▀ ▒█░░▒█ ▒█▄▄▀  ▒█▀▀▀ ▒█░░░ ▒█▄▄█ ░▀▀▀▄▄ ▒█▀▀█ 
▒█░░▒█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄█  ▒█░░░ ▒█▄▄▄█ ▒█░▒█  ▒█░░░ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█░▒█''')
    return;

def startup_flash_programmer():
    global delay
    os.startfile("C:\\Program Files (x86)\\SEGGER\\JLink\\JFlashLite.exe")
    time.sleep(delay)
    #OK
    pyautogui.press("enter")
    #OK
    pyautogui.click(1151, 448 + 70)
    time.sleep(delay)
    return;

def erase_chip(chip_name):
    global delay
    pyautogui.click(1058, 345 + 70)
    time.sleep(delay)
    pyautogui.press(chip_name)
    pyautogui.press("enter")
    time.sleep(1.5)
    return;

def flash_chip(address_hex_file, chip_name):
    global delay
    pyautogui.click(824, 353 + 70)
    time.sleep(delay)
    adress_hex_1 = address_hex_file
    pyperclip.copy(adress_hex_1)
    time.sleep(delay)
    pyautogui.keyDown("ctrl")
    pyautogui.press("v")
    pyautogui.keyUp("ctrl")
    time.sleep(delay)
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press(chip_name)
    pyautogui.press("enter")
    time.sleep(2)
    return;

def close_flash_programer_when_it_open():
    #Close Program
    pyautogui.keyDown("alt")
    pyautogui.press("x")
    pyautogui.keyUp("alt")
    return;

def open_rtt_viewer(chip_name):
    os.startfile("C:\\Program Files (x86)\\SEGGER\\JLink\\JLinkRTTViewer.exe")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.press(chip_name)
    pyautogui.press("enter")
    pyautogui.keyDown("alt")
    pyautogui.press("t")
    pyautogui.press("c")
    pyautogui.keyUp("alt")
    pyautogui.press("enter")
    return;

def windown_to_one_side(side):
    pyautogui.keyDown("win")
    pyautogui.press(side)
    pyautogui.keyUp("win")
    pyautogui.press("enter")
    return;

#MAIN
close_rtt_viewer()
close_flash_programer()
clear_screen()
print_logo()

startup_flash_programmer()
erase_chip("0")
flash_chip("C:\\Work\\code\\my_project\\renesas_workspace\\ek-ra2e1-irc-project\\Debug\\ek-ra2e1-irc-project.hex", "0")
erase_chip("1")
flash_chip("C:\\Work\code\\my_project\\test_workspace\\ek-ra2e1-ira-project\\Debug\\ek-ra2e1-ira-project.hex", "1")
close_flash_programer_when_it_open()
open_rtt_viewer("0")
open_rtt_viewer("1")
windown_to_one_side("right")

#####

pyautogui.alert("Flash was done!", "LEDAT FLASH MACRO PROGRAM")