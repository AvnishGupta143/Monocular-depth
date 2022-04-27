import os
import scipy.misc
from os.path import exists
listFiles = []
counter = 0
for root, dirs, files in os.walk("datacs"):
    for file in files:
        print(counter)
        if file.find("left") == -1:
            file_exists = exists("datacs"+"/"+file[0:file.find('_')] + "/" + file.replace("right","left",1))
            file_exists1 = exists("datacs"+"/"+file[0:file.find('_')] + "/" + file)
            image1 = scipy.misc.imread("datacs"+"/"+file[0:file.find('_')] + "/" + file.replace("right","left",1))
            image2 = scipy.misc.imread("datacs"+"/"+file[0:file.find('_')] + "/" + file)
	    
            if file_exists and file_exists1 and image1.shape[2]==3 and image2.shape[2]==3:
                if counter>=22973:
                    break
                listFiles.append([file[0:file.find('_')] + "/" + file,file[0:file.find('_')] + "/" + file.replace("right","left",1)])
                counter+=1

            
        elif file.find("right") == -1:
            file_exists = exists("datacs"+"/"+file[0:file.find('_')] + "/" + file.replace("left","right",1))
            file_exists1 = exists("datacs"+"/"+file[0:file.find('_')] + "/" + file)
            image1 = scipy.misc.imread("datacs"+"/"+file[0:file.find('_')] + "/" + file.replace("left","right",1))
            image2 = scipy.misc.imread("datacs"+"/"+file[0:file.find('_')] + "/" + file)
            if file_exists and file_exists1 and image1.shape[2]==3 and image2.shape[2]==3:
                if counter>=22973:
                    break
                listFiles.append([file[0:file.find('_')] + "/" + file,file[0:file.find('_')] + "/" + file.replace("left","right",1)])
                counter+=1



print(len(listFiles))
with open('utils/filenames/csDataSetFinal2.txt', 'w') as f:
    for i in range(0, 22973):
        f.write(listFiles[i][0] + " " + listFiles[i][1])
        f.write("\n")



