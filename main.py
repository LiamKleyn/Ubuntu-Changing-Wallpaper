import urllib
import os
import subprocess

print ("Hi, this script by Liam Kleyn will change your wallpaper to a random image from unsplash.it every x minutes, which you can specify, as well as the resolution!")

custom = raw_input("Do you want to automatically set your resolution? Y/N? ")


if custom == 'N':
    userreswidth = raw_input("Please enter your resolution width: ")
    userresheight = raw_input("Please enter your resolution height: ")

    usertime = raw_input("Please enter background change intervals in minutes: ")

    print ("Resolution is,", userreswidth, userresheight)
    print ("Interval is,", usertime)

else:
    print 'If you have 2 monitors, will automatically take the biggest one\'s resolution!'
    output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
    resolution = output.split()[1].split(b'x')

    print output
    print resolution

    width = resolution[0]
    height = resolution[1]

    print 'width is ', width
    print 'height is ', height

    userreswidth = width
    userresheight = height





url = 'https://unsplash.it/' + userreswidth + '/' + userresheight + '/?random'
print url
resource = urllib.urlopen(url)
output = open("background.jpg","wb")
output.write(resource.read())
output.close()
os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/liam/tempclones/Ubuntu-Changing-Wallpaper/background.jpg")
