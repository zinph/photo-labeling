import cv2
from tkinter import filedialog
import os

def file_handler():
    '''Prompt the user for the folder path, and read all the files with it.'''
    #location = input('Please indicate whether right or left you want to label (r, l): ').lower()
    directory = filedialog.askdirectory()
    file_list = os.listdir(directory)
    os.chdir(directory)
    newfolderpath = directory + '/labeled'
    if not os.path.exists(newfolderpath):
        os.mkdir(newfolderpath)
    for each in file_list:
        img = cv2.imread(each)
        #x=60        
        #y=60
        x = int(img.shape[0]/30)
        y = int(img.shape[1]/30)
        #print (x1,y1)
        os.chdir(newfolderpath)
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        labeled = cv2.putText(img,'Arthuzi@Photography',(x,y-5), font , 1.8, (0,0,0),5)
        labeled = cv2.putText(img,'Arthuzi@Photography',(x,y), font , 1.8, (255,255,255),6)
        labeled = cv2.putText(img,'Arthuzi@Photography',(x,y+5), font , 1.8, (0,0,0),4)
        #labeled = cv2.putText(img,'Arthuzi@Photography',(x,y+8), font , 1.5, (255,255,255),2)
        newfile = 'l-'+each
        if os.path.exists(newfolderpath+'/'+newfile):
            os.remove(newfile)
        cv2.imwrite(newfile, labeled)
        os.chdir(directory)

file_handler()
