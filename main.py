import os
import network

# 默認「ins」爲「insta;;」、mod爲「module」
def check_efi()->bool:
    return os.path.isdir("ls /sys/firmware/efi/efivars")
def start_display():
    print("""
    这里是Cleararch Team，欢迎你安装我们的系统！
    这段文字的写作者：Kirisame Marisa对你表示真诚的问候。
    本系统以Arch为基础，加入了许多「原创的」软件包、配置等，团队均为中国人，相信能让同在中国的你更感熟悉。
    本项目借鉴了大量Clear linux的思想，所以我们拼合两个发行版的名字，也就是「Cleararch」。
    请谨慎的考虑使用一个滚动发行的、小团队维护的Linux，这可能并不适合您。
    如果您考虑周全了，按下「回车键」来进入下一步（连接因特网）。
    """)
    input()
    os.system("timedatectl set-ntp true")
    if not network.check_networking():
        network.connect_network()

