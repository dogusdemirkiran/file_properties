import magic
import sys
import os,time
import subprocess

file = str(sys.argv[1]) #Target File
out = open("analysis.txt","w") #Out File

file_type = magic.from_file(file, mime=True)
out.write("File Path: " + file +"\n")
out.write("File Type: "+ file_type+"\n")

file_size = os.path.getsize(file)
file_size = file_size / 1024
file_size = str(file_size)
out.write("File Size: " + file_size + " kB" + "\n")

stat = os.stat(file)

##Modification Date##
yil = time.localtime(stat.st_mtime).tm_year
ay = time.localtime(stat.st_mtime).tm_mon
gun = time.localtime(stat.st_mtime).tm_mday
saat = time.localtime(stat.st_mtime).tm_hour
dakika = time.localtime(stat.st_mtime).tm_min
saniye = time.localtime(stat.st_mtime).tm_sec
yil = str(yil)
ay = str(ay)
gun = str(gun)
saat = str(saat)
dakika = str(dakika)
saniye = str(saniye)
out.write("File Modification Date: " + yil +"."+ay+"."+gun+"   "+saat+":"+dakika+":"+saniye + "\n")


##Change Date##
c_yil = time.localtime(stat.st_ctime).tm_year
c_ay = time.localtime(stat.st_ctime).tm_mon
c_gun = time.localtime(stat.st_ctime).tm_mday
c_saat = time.localtime(stat.st_ctime).tm_hour
c_dakika = time.localtime(stat.st_ctime).tm_min
c_saniye = time.localtime(stat.st_ctime).tm_sec
c_yil = str(c_yil)
c_ay = str(c_ay)
c_gun = str(c_gun)
c_saat = str(c_saat)
c_dakika = str(c_dakika)
c_saniye = str(c_saniye)
out.write("File Change Date: " + c_yil +"."+c_ay+"."+c_gun+"   "+c_saat+":"+c_dakika+":"+c_saniye + "\n")


##Access Date##
a_yil = time.localtime(stat.st_atime).tm_year
a_ay = time.localtime(stat.st_atime).tm_mon
a_gun = time.localtime(stat.st_atime).tm_mday
a_saat = time.localtime(stat.st_atime).tm_hour
a_dakika = time.localtime(stat.st_atime).tm_min
a_saniye = time.localtime(stat.st_atime).tm_sec
a_yil = str(a_yil)
a_ay = str(a_ay)
a_gun = str(a_gun)
a_saat = str(a_saat)
a_dakika = str(a_dakika)
a_saniye = str(a_saniye)
out.write("File Access Date: " + a_yil +"."+a_ay+"."+a_gun+"   "+a_saat+":"+a_dakika+":"+a_saniye + "\n")

##File Permission
out.write("File Permission: " + (oct(stat.st_mode)[-3:]))

#ldd File Shared(Dynmaic) Lib
out.write("\nShared(Dynamic) Files(.so): \n")
ldd = subprocess.Popen(['ldd',file],stdout=subprocess.PIPE)
for line in ldd.stdout:
    line = str(line,'utf-8')
    out.write(line)