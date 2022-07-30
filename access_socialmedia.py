import os
import datetime
import time
import webbrowser


def Shutdown():
    os.system("shutdown /s /t 1")

def Restart():
    os.system("shutdown /r /t 1")

def Facebook():
    url='https://www.facebook.com/'
    webbrowser.register("chrome",None,webbrowser.BackgroundBrowser("E://yaswanth//practise//Application//chrome.exe"))
    webbrowser.get('chrome').open_new(url)

def Whatsapp():
    url='https://web.whatsapp.com/'
    webbrowser.register("chrome", None,webbrowser.BackgroundBrowser("E://yaswanth//practise//Application//chrome.exe"))
    webbrowser.get("chrome").open_new(url)

def Instagram():
    url='https://www.instagram.com/accounts/login/?hl=en'
    webbrowser.register("chrome", None,webbrowser.BackgroundBrowser("E://yaswanth//practise//Application//chrome.exe"))
    webbrowser.get("chrome").open_new(url)

def Youtube():
    url='https://www.youtube.com/'
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("E://yaswanth//practise//Application//chrome.exe"))
    webbrowser.get("chrome").open_new(url)

def Twitter():
    url='https://twitter.com/'
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("E://yaswanth//practise//Application//chrome.exe"))
    webbrowser.get("chrome").open_new(url)


print("1.Shutdown")
print("2.Restart")
print("3.Open Web whatsapp")
print("4.Open Facebook.")
print("5.Open Instagram.")
print("6.Open Twitter")
print("7.Open Youtube")

e=1
while e>0:
    A=int(input("Enter number : "))
    if A==1:
        Shutdown()
        break
    elif A==2:
        Restart()
        break
    elif A==3:
        Whatsapp()
        break
    elif A==4:
        Facebook()
        break
    elif A==5:
        Instagram()
        break
    elif A==6:
        Twitter()
        break
    elif A==7:
        Youtube()
        break
    else:
        print("please enter a valid command")
        e=int(input("Enter '0' to exit or any key to continue : "))






