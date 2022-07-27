import os,json


def mod_ins(mod_list : list,
            introduction_list : list,
            addation_dict : dict,
            ins_dir="/mnt",
            a=-1) -> bool:
    # mod_list : 可安裝列表 introduction_list : 安裝紹介 ins_dir : 安裝目錄 a : 安裝序號
    if mod_list != list and introduction_list != list and addation_dict != dict:
        return False
    if len(mod_list)!=len(introduction_list) or len(mod_list)==0:
        return False
    for i,b in addation_dict:
        if i != int:
            return False
        if i<0:
            return False
    n=-1
    for i in mod_list:
        n+=1
        print(i,"\t意義", introduction_list[n])
    if a==-1:
        a = input("選項：")
        try:
            a=int(a)
        except TypeError:
            print("錯誤：輸入非數字。")
            input("請橋下「回車」再來一遍")
            mod_ins(mod_list, introduction_list,addation_dict,ins_dir=ins_dir)
        if a>len(mod_list) or a<0:
            print("錯誤：輸入值大於或小於索引。")
            input("請橋下「回車」再來一遍")
            mod_ins(mod_list, introduction_list,addation_dict, ins_dir=ins_dir)
    if os.system("yes |  pacstrap  "+mod_list[a]):
        os.system("clear")
        return False
    else:
        os.system("clear")
        return True

def install_from_json(json_file):
    f = open(json_file,"r",encoding="utf8")
    install_text = json.load(f)
    try:
        return mod_ins(install_text[0],install_text[1],install_text[2],install_text[3])
    except IndexError:
        try:
            return mod_ins(install_text[0],install_text[1],install_text[2])
        except IndexError:
            return False
