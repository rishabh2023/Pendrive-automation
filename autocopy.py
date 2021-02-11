import os
import shutil
import time
while True:

    try:
        path = 'D:'
        a = os.listdir(path)
        final = []
        for i in a:
            if '.pptx' in i :
                final.append(i)
            elif '.ppt' in i :
                final.append(i)


        for j in final:
            if j[-6:-8:-1] == '11'or j[-11:-13:-1] == '11' or j[-5:-7:-1] == '11' or j[-9:-11:-1]=='11' or j[-10:-12:-1] == '11':
                source = "D:"+'\{}'.format(j)
                destination = 'C:\Studentsfiles\{}'.format(j)
                dest = shutil.copyfile(source,destination)
                print('File Copied successfully Please Remove the Pendrive..')
                print('Please Insert next Pendrive')
                time.sleep(4)
            else:
                print('File is not in Right Format..')


    except:
        print('Pendrive Not Found Please Insert it....')
        time.sleep(1)
    