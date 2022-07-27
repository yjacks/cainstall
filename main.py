import os
import network

# 默認「ins」爲「insta;;」、mod爲「module」
def check_efi()->bool:
    return os.path.isdir("ls /sys/firmware/efi/efivars")
def start_display():
    print("""
    這裏是Cleararch Team，歡迎你安裝我們的系統！
    這段文字的寫作者：Kirisame Marisa對你表示真誠的問候。
    本系統以Arch爲基礎，加入了許多「原創的」軟體包、配置等，團隊均爲中國人，相信能讓同在中國的你更感熟悉。
    本項目借鑑了大量Clear linux的思想，所以我們拼合兩個發行版的名字，也就是「Cleararch」。
    請謹慎的考慮使用一個滾動發行的、小團隊維護的Linux，這可能並不適合您。
    如果您考慮周全了，按下「回車鍵」來進入下一步（連接網際網路）。
    """)
    input()
    os.system("timedatectl set-ntp true")
    if not network.check_networking():
        network.connect_network()

