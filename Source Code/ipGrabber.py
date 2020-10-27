import socket
import tkinter as tk
###########################################################################
def ipGrabber(): #Reads host name & ip address
    global hostName,IP
    hostName=socket.gethostname()
    IP=socket.gethostbyname(hostName)
    
    results()
###########################################################################
def results(): #Outputs results
    resultsUI=tk.Tk()
    resultsUI.resizable(0,0)

    tk.Label(resultsUI,text="Thanks for your info (:").pack()
    tk.Label(resultsUI,text="Just in case you wanted it:").pack()
    tk.Label(resultsUI,text=("Host Name: "+hostName)).pack()
    tk.Label(resultsUI,text=("IP:",IP)).pack()
    tk.Button(resultsUI,text="Take the L and exit",command=resultsUI.destroy,bd=2).pack()

    resultsUI.mainloop()
###########################################################################
ipGrabber()
