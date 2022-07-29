import os
import network


# 默认「ins」为「install」、「mod」为「module」
def check_efi() -> bool:
    return os.path.isdir("ls /sys/firmware/efi/efivars")


def start_display() -> None:
    print(
        "这里是 ClearArch 开发团队，欢迎您安装 ClearArch！\n"
        "本系统基于 Arch Linux，并加入许多原创软件包、配置等内容。\n"
        "在创新的同时，我们也借鉴大量 Clear Linux 的思想，项目由此得名。\n"
        "因本系统滚动发行并由小团体维护，请谨慎考虑使用。\n"
        "若您考虑周全并愿意承担风险，请按下 Enter 以进入下一步。\n"
        "\n"
        "Welcome to the ClearArch installer!\n"
        "ClearArch takes several ideas and concepts from Clear Linux and implements them onto an Arch platform.\n"
        "This makes the core of the project, which is further innovated on with the introduction of several new packages and configurations.\n"
        "\n"
        "Be advised that this project is released and maintained by a small group on a rolling basis, so exercise caution when installing it.\n"
        "If you understand and are willing to take the risk, press Enter to proceed to the next step."
        )
    input()

    # 检测网络
    if not network.check_networking():
        network.connect_network()

    os.system("timedatectl set-ntp true") # 时区设置应当在网络连接之后进行
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

