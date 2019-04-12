import random
import time
import os

direct = os.chdir("/storage/emulated/0/")
try:
    os.makedirs("Mouta7at")
    os.chdir("/storage/emulated/0/Mouta7at")
except:
    os.chdir("/storage/emulated/0/Mouta7at")

print("""
                        _           _____ 
   /\/\    ___   _   _ | |_   __ _ |___  |
  /    \  / _ \ | | | || __| / _` |   / / 
 / /\/\ \| (_) || |_| || |_ | (_| |  / /  
 \/    \/ \___/  \__,_| \__| \__,_| /_/   
                                          
     coded by : \33[93mHunter Follow\33[97m

Facebook : \33[93mAbderrazak A.\33[97m
Instagram : \33[93mhn_flw\33[97m
Github : \33[93mHunter Follow\33[97m
""")
name = str(input("\n[\33[96m*\33[97m] Name (الاسم) : \33[93m"))

file_name = str(input("\n\33[97m[\33[96m*\33[97m] Give the file a name (اسم الملف) : \33[93m"))
if ".txt" in file_name:
    file_name_2 = file_name + ""
elif ".txt" not in file_name:
    file_name_2 = file_name + ".txt"
    
file = open(file_name_2, "w")

mail = "@hotmail.com"
gmail = "@gmail.com"
yahoo = "@yahoo.com"

choice = str(input("\n\33[97m[\33[91m!\33[97m] chose (اختر) : \n    [\33[91m1\33[97m] Hotmail\n    [\33[91m2\33[97m] Gmail\n    [\33[91m3\33[97m] Yahoo\n\n>> : \33[93m"))
if choice == "1":
    mail = "@hotmail.com"
elif choice == "2":
    mail = gmail
elif choice == "3":
    mail = yahoo
    
def writer():
    for i in range(100):
        pick = str(random.randint(0, 100))
        pick_2 = str(random.randint(0, 100))
        file.write(name + pick + mail + "\n")
        file.write(name + pick + pick_2 + mail + "\n")
        file.write(name + "_" + pick + mail + "\n")
        file.write(name + "_" + pick + pick_2 + mail +  "\n")
        file.write(name + "_" + pick + "_" + pick_2 + mail + "\n")

def years():
    for i in range(50):
        year = str(random.randint(1960, 2010))
        file.write(name + year + mail + "\n")
        file.write(name + "_" + year + mail + "\n")
writer()
years()
file.close()

print("\n\33[97m[\33[91m•\33[97m] Writing mails...\n            جاري كتابة الايمايلات...")
time.sleep(1)
print("\n[\33[92m✅\33[97m] Done\33[97m")

while True:
    choice_2 = str(input("\n\n    [\33[91m1\33[97m] Make more mails (صنع المزيد)\n    [\33[91m0\33[97m] Exit (خروج)\n\n>> : \33[93m"))
    if choice_2 == "1":
        name = str(input("\n\33[97m[\33[96m*\33[97m] Name (الاسم) : \33[93m"))
        file_name = str(input("\n\33[97m[\33[96m*\33[97m] Give the file a name (اسم الملف) : \33[93m"))
        if ".txt" in file_name:
            file_name_2 = file_name + ""
        elif ".txt" not in file_name:
            file_name_2 = file_name + ".txt"
        file = open(file_name_2, "w")
        choice = str(input("\n\33[97m[\33[91m!\33[97m] chose (اختر) : \n    [\33[91m1\33[97m] Hotmail\n    [\33[91m2\33[97m] Gmail\n    [\33[91m3\33[97m] Yahoo\n\n>> : \33[93m"))
        if choice == "1":
            mail = "@hotmail.com"
        elif choice == "2":
            mail = gmail
        elif choice == "3":
            mail = yahoo
        writer()
        years()
        file.close()
        print("\n\33[97m[\33[91m•\33[97m] Writing mails...\n            جاري كتابة الايمايلات...")
        time.sleep(1)
        print("\n[\33[92m✅\33[97m] Done\33[97m")
    elif choice_2 == "0":
        print("\n\n\33[97mThanks for using \33[93mMouta7 \33[97m! Bye..")
        exit()