import os
import time
from zipfile import ZipFile

class bcolors:
    RED = '\033[91m'

def banner():
    print(bcolors.RED + '+[+[+[ Zip-Bomber ]+]+]+')
    print(bcolors.RED + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.RED + '''
                     \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,      ___ ..__ .__         .
             |#########################|       / ||__|[__) _ ._ _ |_  _ ._.
            |###########################|     /__||   [__)(_)[ | )[_)(/,[
           |#############################|  
           |#############################|              
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')



def get_extracted_size(filepath: str) -> int:

    zp = ZipFile(filepath)
    name = zp.infolist()
    if zp.infolist()[0].file_size*0.23 > zp.infolist()[0].compress_size:
        return -1
    pathname = zp.infolist()[0].filename
    return sum([zinfo.file_size for zinfo in zp.filelist])

def unzip (path, total_count,depth):
    if depth>5:
        return -1
    time.sleep(1)

    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            
            if (not file_name.endswith('.zip')):
                total_count += 1
            else:
                num = get_extracted_size(root+"/"+ file)
                if num == -1:
                    return -1
                currentdir = file_name[:-4]
                if not os.path.exists(currentdir):
                    os.makedirs(currentdir)
                with ZipFile(file_name) as zipObj:
                    zipObj.extractall(currentdir)
                os.remove(file_name)
                
                total_count = unzip(currentdir, total_count,depth+1)

                if total_count== -1:
                    return -1
    return total_count

total_count = unzip ('.', 0,1)
if total_count !=-1:
    print('healthy file')
else:
    banner()


