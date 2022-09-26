'''
WK-6 STARTER SCRIPT
CYBV 312
Professor Hosmer
FEBRUARY 2022
'''

# Python Standard Libaries 
import os
import re
import logging
import platform
import socket
import uuid

import psutil  # pip install psutil

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False


def main():
    
    # Remove any old logging script
    if os.path.isfile('YOURNAME-ScriptLog.txt'):   # REPLACE YOURNAME with Your Name
        os.remove("YOURNAME-ScriptLog.txt")
    
    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='Kristin Skipper-ScriptLog.txt', level=logging.DEBUG, format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")
    
    investigator = input("Investigator Name:  ")   # Enter Your Name at this prompt
    organization = input("Class Code  :       ")   # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION
    
    sysInfo = getSystemInfo()
    
    if sysInfo:
        ''' YOUR CODE GOES HERE 
            Write all collected information to the log file
        '''  
if __name__ == '__main__':
    
    print("\n\nWeek-6 Logging Starter Script - YOUR NAME \n")
    main()
    print("\nScript End")

