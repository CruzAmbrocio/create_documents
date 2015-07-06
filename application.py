'''create fles'''
import time
import os
import os.path
import mock
import sys
#to clear screen
def reset():
    """Used to reset the screen"""
    os.system("reset")
#function of menu
def menu():
    reset()
    print"  "
    print "---Welcome ---"
    print ""
    print "   If you want crate archive type -- 1 --"
    print "   If you want deleted Document type -- 2 --"
    print "   To exit type -- 3 --"
    print " "
    while True:
        num = raw_input(" > Choose an option:  ")
        if num == "1":
            reset()
            print "-- Document Creator --"
            print "  "
            creation()
        elif num == "2":
            reset()
            print "--- Delete Files ---"
            delete()
        elif num == "3":
            print "Bye....."
            time.sleep(1)
            reset()
            sys.exit(1)
        else:
            print "Enter a valid option"
            menu()
#Enter name
def name():
    enter_name = raw_input("> Type the name of Document :  ")
    return enter_name
#verification of existence of pach of file
def verification(files):
    return os.path.isfile(files + '.txt')
#verification existence for creation file
def creation():
    file_name = name()
    is_file = verification(file_name)
    if is_file == True:
        reset()
        print "El fichero existe"
        print "   "
        print "--- Enter a valid name ---"
        raw_input("--- Press Enter ---")
        menu()
    elif is_file == False:
        reset()
        print "El fichero no existe"
        print "   "
        raw_input("--- Press Enter to create ")
        create(file_name)
#function for creation file
def create(name_file):
    archi = open(name_file + '.txt', 'w')
    archi.close()
    time.sleep(0.5)
    print "-- Document Created --"
    time.sleep(1)
    menu()
#verification existence of file
def delete():
    file_name = name()
    is_file = verification(file_name)
    if is_file == True:
        reset()
        print "El fichero existe"
        print "  "
        raw_input("--- Press enter to deleted ---")
        remove(file_name)
        time.sleep(0.5)
        menu()
    elif is_file == False:
        reset()
        print "El fichero no existe"
        print "   "
        print "--- Enter a valid name ---"
        raw_input("--- Press Enter  ")
        menu()
#function for delete file 
def remove(verify):
    os.remove(verify + '.txt')

if __name__ == '__main__':
    menu()
