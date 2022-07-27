import os
from urllib.request import urlopen

import multi_lang
lang=multi_lang.name("zh_CN")

def check_networking():
    myURL1 = urlopen("https://www.quad9.net")
    if myURL1.getcode()!=200:
        return False
    else:
        return  True


def connect_network():
    # 列出可用网络
    print(lang.listingNetwork+"\n")
    os.system("nmcli device wifi list")
    while True:
        userInputSSID = input(lang.inputNetworkSSID)
        if userInputSSID == "":
            print(lang.emptyNetworkSSID)
        else:
            userInputPwd = input(lang.inputNetworkPwd)
            if userInputPwd == "": # 无密码情况
                os.system("nmcli device wifi connect %s" %(userInputSSID))
                return check_networking()
            else: # 包含密码
                os.system("nmcli device wifi connect %s password %s" %(userInputSSID, userInputPwd))
                return check_networking()