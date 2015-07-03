import os
import sys
import time
def menu():
    reset()
    print"  "
    print "---Welcome ---"
    print ""
    print "   If you want crate archive type -- 1 --"
    print "   If you want deleted Document type -- 2 --"
    print "   To exit type -- 3 --"
    print " "
    true=1
    while true==1:
        num=raw_input(" > Choose an option:  ")
        if num == "1":
            reset()
            print "-- Document Creator --"
            print "  "
            veryfication()
        elif num == "2":
            reset()
            print "--- Delete Files ---"
            remove()
        elif num =="3" :
            print "Bye....."
            time.sleep(1)
            clear()
            sys.exit(1)
        else:
            print "Enter a valid option"
            menu()

def reset():
        """Used to reset the screen"""
        os.system ("reset")

def name():
    name=raw_input("> Type the name of Document :  ")
    return name

def remove():
    print "   "
    verify=name()
    try: 
        fichero = open(verify+'.txt') 
        fichero.close()
        reset()
        print "El fichero existe"
        print "  "
        raw_input( "--- Press enter to deleted ---")
        fichero = os.remove(verify+'.txt')
        time.sleep(0.5)
        menu()
    except: 
        reset()
        print "El fichero no existe"
        print "   "
        print "--- Enter a valid name ---"
        raw_input ("--- Press Enter  ")
        menu()

def veryfication():
    print "   "
    verify=name()
    try: 
        fichero = open(verify+'.txt') 
        fichero.close() 
        reset()
        print "El fichero  existe"
        print "   "
        print "--- Enter a valid name ---"
        raw_input ("--- Press Enter  ")
        menu()
    except: 
        print "El fichero no existe"
        creaciontxt(verify)

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def creaciontxt(hola):
    time.sleep(0.5 )
    archi=open(hola+'.txt','w')
    archi.close()
    time.sleep(0.5)
    print "-- Document Created --"
    time.sleep(1)
    menu()

menu()
