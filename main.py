import os
import network


# 默認「ins」爲「insta;;」、mod爲「module」
def check_efi() -> bool:
    return os.path.isdir("ls /sys/firmware/efi/efivars")


def start_display() -> None:
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
    os.system("clear")
    print("下一步是使用cfdisk分区，请选择硬碟设备文件，然后按回车键，输入「list」以查看硬碟（按q以退出）。")

    def list_disk():
        if input("") == "list":
            os.system("fdisk -l | less")
            if input("请记住硬碟设备文件列表，输入「exit」进入下一步") != "exit":
                list_disk()

    def select_disk():
        a = input()
        if a == "list":
            list_disk()
        else:
            if not os.path.isfile(a) or not a.find("/dev"):
                print("硬碟设备文件选择错误，请再次输入，输入「list」可查看硬碟")
                select_disk()
            else:
                return a

    a = select_disk()
    while True:
        if os.system("cfdisk " + a) != 0:
            print("硬碟设备文件错误，返回上一层")
            continue
        else:
            break
    print("""
    录入分区表
    请输入您分的区，格式：
    硬碟设备文件 类型
    类型列表：
    root 根
    usr /usr    tmp /tmp    home /home
    swap swap   boot /boot  opt /opt
    etc /etc 
    efi 非uefi环境:输入被忽略
    uefi环境，boot未创建 /boot
    uefi环境，boot被创建 /boot/efi
    mount_point 其它，请注明挂载点
    输入exit以退出
    若挂硬盘设备文件无效
    """)
    def input_disk() -> dict:
        disk={}
        if check_efi():
            while True:
                a = input()
                if a != "exit":
                    disk.update(a)
        else:
            while True:
                a = input()
                if a == "efi":
                    continue
                if a != "exit":
                    disk.update(a)
        return disk
    disk = input_disk()
    n=True
    b=0
    while n:
        for i,a in disk:
            if not os.path.isfile(a) or not a.find("/dev"):
                if a == "root":
                    b+=1
                    print("root分区错误，请重新输入")
                    break
        if n:
            if not b:
                break
            b=0
            disk = input_disk()

