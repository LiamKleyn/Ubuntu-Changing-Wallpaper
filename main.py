import urllib
import os


print ("Hi, this script by Liam Kleyn will change your wallpaper to a random image from unsplash.it every x minutes, which you can specify, as well as the resolution!")
userreswidth = raw_input("Please enter your resolution width: ")
userresheight = raw_input("Please enter your resolution height: ")

usertime = raw_input("Please enter background change intervals in minutes")

print ("Resolution is,", userreswidth, userresheight)
print ("Interval is,", usertime)




url = 'https://unsplash.it/' + userreswidth + '/' + userresheight + '/?random'
print url
resource = urllib.urlopen(url)
output = open("background.jpg","wb")
output.write(resource.read())
output.close()

os.system("gsettings set org.gnome.desktop.background picture-uri file:/home/liam/tempclones/Ubuntu-Changing-Wallpaper/background.jpg")
