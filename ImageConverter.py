#Author : Ibrahim Sydock
#Date   : Tue Feb 23 19:38:48 2021
#File   : ImagerConverter.py (Lab 10)

from PIL import Image
import glob, os

# New Code

OUTPUT_PATH = r'output'

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

for infile in glob.glob("*.*"):
    file, ext = os.path.splitext(infile)
    if ext == ".jpg" or ext == ".png": 
        with Image.open(infile) as im:
                im.convert('L').resize((int(im.width/2),int(im.height/2))).save("output\\" + file + ext, "PNG")

'''
Before:
#Original Images
img1 = Image.open('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\Lab10Images\cwu_logo0.jpg')
img2 = Image.open('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\Lab10Images\cwu_logo1.png')
img3 = Image.open('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\Lab10Images\cwu_logo2.jpg')
img4 = Image.open('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\Lab10Images\cwu_logo3.jpg')
img5 = Image.open('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\Lab10Images\cwu_logo4.png')
img6 = Image.open('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\Lab10Images\cwu_logo5.jpg')

#New Converted Images, Saved
nImg1 = img1.convert('L').resize((int(img1.width/2),int(img1.height/2))).save('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\grey_resized_logos\cwu_logo0.jpg')
nImg2 = img2.convert('L').resize((int(img2.width/2),int(img2.height/2))).save('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\grey_resized_logos\cwu_logo1.png')
nImg1 = img3.convert('L').resize((int(img3.width/2),int(img3.height/2))).save('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\grey_resized_logos\cwu_logo2.jpg')
nImg1 = img4.convert('L').resize((int(img4.width/2),int(img4.height/2))).save('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\grey_resized_logos\cwu_logo3.jpg')
nImg1 = img5.convert('L').resize((int(img5.width/2),int(img5.height/2))).save('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\grey_resized_logos\cwu_logo4.png')
nImg1 = img6.convert('L').resize((int(img6.width/2),int(img6.height/2))).save('C:\\Users\\shark\\OneDrive\\Documents\\College Documents\\Winter Quarter 2021\\CS 112\\Labs\\Lab 9\\grey_resized_logos\cwu_logo5.jpg')
'''