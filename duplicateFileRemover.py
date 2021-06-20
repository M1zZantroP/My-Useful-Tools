import hashlib
import os
import time

print("*****  Welcome to MizZantroP's cleaner!  *****")
time.sleep(1.5)

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

lib = input('Enter path to check for duplicate:  \n--->  ')
clear_screen()

def checker(directory = lib):
    files_for_check = os.listdir(directory)
    print('    I find  ---> %s objects here' % len(files_for_check))
    single = []
    unique_hash = []
    to_remove = []

    for i in files_for_check:
        if hashlib.md5(open(directory + i, 'rb').read()).hexdigest() not in unique_hash:
            unique_hash.append(hashlib.md5(open(directory + i, 'rb').read()).hexdigest())
            single.append(i)
        else:
            to_remove.append(i)

    return to_remove

def remover():
    status = 0
    print('DO YOU REALLY WANT TO REMOVE ALL THE --> %s <-- FILES?!' % len(checker()))
    print('    Press -Y/y- for continue')
    print('    Press any key for exit')
    temp = input('    --->  ')
    if temp == 'Y' or temp == 'y':
        for i in checker():
            os.remove(lib + i)
            status += 1
        return 'Removed: %s duplicate objects' % status
    else:
        return 'Exiting... .'


if __name__ == '__main__':
    start_time = time.time()
    print(remover())
    print('Finished in: %s sec.' % round(time.time() - start_time, 3))
    print('-----------------------------')
    print('Have a nice day!')