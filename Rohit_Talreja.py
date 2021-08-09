"""
@Author : Rohit Talreja
@Created On: 31-07-2021
@Title: Port Scanner
"""

#!/bin/python3 #Generally used in kali. (#! is shebang.)
# boiler plate of Sample Port Scanner
#It isn't perfect. We can't get everything in very beginning. Its a bad port scanner.

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv)==2:
        target = socket.gethostbyname(sys.argv[1]) #Translates hostname to IPv4
else:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner - Just for fun!!!
print("-" * 70)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 70)

try:
          for port in range(1,65535): #Depends on how much range you want to put in, if you know which port is open in that ip address... cause its so, lengthy and time taking.
          		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       			socket.defaulttimeout(1)
                result= s.connect_ex((target,port))                                  #It returns an error indicator.
                print("Checking port {}".format(port))   #It is optional depends on you whether wanna write it or not. Cause this line of code will umm... not gonna break suspense, run it see for yourself. Its fun!!!
                if result == 0:
                       print("Port {} is open".format(port))
                else
                  	   print("Port {} is not open".format(port))
                s.close()


except KeyboardInterrupt: #KeyboardInterrupt
	print("\nKeyboard Interruption Error")
	sys.exit()

except  socket.gaierror:  #hostname could not be resolved
	print("Host Name could not be resolved.")
	sys.exit()

except  socket.error:  #couldn't connect to server
	print("Could not connect to server")
	sys.exit()
