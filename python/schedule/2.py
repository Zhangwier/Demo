import tkinter as tk
import time
import os
import json


#封装成app!
class Schedule_app():

    def __init__(self):
        pass

    #设置读取
    def begin_road(self):
        pass

    #向服务器发送数据
    def send_massage(self,data):
        pass

    #接收数据
    def accept_massage(self):
        data=""
        return data


#桌布
class basedesk():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('My assistant')
        self.root.geometry('600x400')
        self.root.minsize(600, 400) # 最小尺寸
        self.root.maxsize(600, 400) # 最大尺寸
        #self.root.config()
        self.schedule_adr=""
        self.library_adr="C:\\Users\\考拉\\Documents\\_JB\\python\\library.txt"
        self.logs_adr=""
        self.setting_adr=""#需要加载


def TxtPrint(txt):
    print(txt)


def load_data(file_name):

    def formatting_file_name(file_name):
        if not file_name.split(".")[-1]:
            TxtPrint("Error!Enter a filename with a formatted suffix.")
        elif file_name.split(".")[-1] not in ("txt", "json"):
            TxtPrint(
                "This format cannot be converted, please contact the author to update.")
            file_name = file_name.split(".")[0]
        else:
            return file_name.split(".")[-1]
        TxtPrint("We will road in text format.")
        return "txt"

    def Ctxt(file_name):
        data = {}
        with open(file_name, mode="r", encoding="utf-8") as f:
            for _ in f.readlines():
                data[_.split()[0]]= _.split()[1]
        return data

    def Cjson(file_name):
        data = json.load(file_name)
        return data

    def Csql(fil_name):
        pass

    # 表驱动
    format_load_dir = {"txt": Ctxt, "json": Cjson, "sql": Csql}
    file_format = formatting_file_name(file_name)
    return format_load_dir[file_format](file_name)


def get_txt(file_adr):
    try:
        with open(file_adr,mode="r",encoding="utf-8") as f:
            file_data=f.read()
    except:
        file_data="cant open file:"+file_adr+" !"
    return file_data


def save_file_data(file_adr,save_data):
    try:
        with open(file_adr,mode="w",encoding="utf-8") as f:
            f.write(save_data)
    except:
        #错误处理
        pass


def main_screen():
    main_frame = tk.Frame(master=root.root)
    schedule_button = tk.Button(main_frame,text='Schedule',\
        command=schedule_screen,width=10, height=1)
    aitalk_button = tk.Button(main_frame,text='AI talk',\
        command=aitalk_screen,width=10, height=1)
    library_button = tk.Button(main_frame,text='Library',\
        command=library_screen,width=10, height=1)
    logs_button = tk.Button(main_frame,text='Logs',\
        command=logs_screen,width=10, height=1)
    setting_button = tk.Button(main_frame,text='setting',\
        command=setting_screen,width=10, height=1)
    canvas = tk.Canvas(main_frame, bg='white', height=200, width=400)
    #image_file = tk.PhotoImage(file='pic.gif')
    #image = canvas.create_image(200, 0, anchor='n',image=image_file)

    canvas.pack(side=tk.TOP,pady=6)
    schedule_button.pack(side=tk.TOP,pady=6)
    library_button.pack(side=tk.TOP,pady=6)
    logs_button.pack(side=tk.TOP,pady=6)
    setting_button.pack(side=tk.TOP,pady=6)
    #"""
    global now_frame
    now_frame.destroy()
    now_frame = main_frame
    main_frame.pack()


def schedule_screen():
    schedule_frame = tk.Frame(master=root.root)
    back_botton = tk.Button(schedule_frame,text='BACK',\
        command=main_screen,width=10, height=1)

    back_botton.pack(anchor=tk.S, side=tk.RIGHT,padx=10, pady=10)

    global now_frame
    now_frame.destroy()
    now_frame = schedule_frame
    schedule_frame.pack()


def library_screen():
    library_frame = tk.Frame(master=root.root)
    open_library_botton = tk.Button(library_frame,text='open',\
        command=lambda:show_in_txt(library_show,data=get_txt(root.library_adr)),width=10, height=1)
    save_library_botton = tk.Button(library_frame,text='save',\
        command=lambda:save_file_data(root.library_adr,library_show.get(1.0, "end")),width=10, height=1)
    back_botton = tk.Button(library_frame,text='BACK',\
        command=main_screen,width=10, height=1)
    library_show = tk.Text(library_frame,width=40, height=20)

    library_show.pack(anchor=tk.S, side=tk.RIGHT,padx=5, pady=5)
    open_library_botton.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=10)
    save_library_botton.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=10)
    back_botton.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=10)

    global now_frame
    now_frame.destroy()
    now_frame = library_frame
    library_frame.pack()


def aitalk_screen():
    aitalk_frame = tk.Frame(master=root.root)
    back_botton = tk.Button(aitalk_frame,text='BACK',\
        command=main_screen,width=10, height=1)

    back_botton.pack(anchor=tk.S, side=tk.RIGHT,padx=10, pady=10)

    global now_frame
    now_frame.destroy()
    now_frame = aitalk_frame
    aitalk_frame.pack()


def logs_screen():
    logs_frame = tk.Frame(master=root.root)
    back_botton = tk.Button(logs_frame,text='BACK',\
        command=main_screen,width=10, height=1)

    back_botton.pack(anchor=tk.S, side=tk.RIGHT,padx=10, pady=10)

    global now_frame
    now_frame.destroy()
    now_frame = logs_frame
    logs_frame.pack()


def setting_screen():
    try:
        setting_dir=json.load(root.setting_adr)
        for _ in setting_dir:
            exec("_[0]=x",{"x":_[1]})
    except:
        setting_dir={}
        setting_dir["root.schedule_adr"]="schedule.txt"
        setting_dir["root.library_adr"]="library.txt"
        setting_dir["root.logs_adr"]="logs.txt"
        setting_dir["root.setting_adr"]="setting.txt"
        #格式
        with open("setting.json",mode="w",encoding="utf-8") as f:
            f.write(json.dumps(setting_dir, sort_keys=True, indent=4, separators=(',', ': ')))

    setting_frame = tk.Frame(master=root.root)

    change_schedule_botton = tk.Button(setting_frame,text='change',\
        command=main_screen,width=10, height=1)
    change_all_label = tk.Label(setting_frame, text=\
        'Schedule address\n\n\nLibrary address\n\n\nLogs address\n\n\nSetting address', \
        width=15, height=13)
    change_schedule_entry = tk.Entry(setting_frame,width=20)
    change_library_entry = tk.Entry(setting_frame,width=20)
    change_logs_entry = tk.Entry(setting_frame,width=20)
    change_setting_entry = tk.Entry(setting_frame,width=20)
    change_all_botton = tk.Button(setting_frame,text='change',\
        command=lambda:change_setting_adr(setting_dir,[change_schedule_entry.get(),\
            change_library_entry.get(),\
                change_logs_entry.get(),\
                    change_setting_entry.get()\
                        ]),width=10, height=1)
    back_botton = tk.Button(setting_frame,text='BACK',\
        command=main_screen,width=10, height=1)

    change_all_label.pack(anchor=tk.N, side=tk.LEFT,padx=0, pady=2)
    change_schedule_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=30)
    change_library_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=13)
    change_logs_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=20)
    change_setting_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=20)
    change_all_botton.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=15)
    back_botton.pack(anchor=tk.S, side=tk.BOTTOM,padx=2, pady=2)

    global now_frame
    now_frame.destroy()
    now_frame = setting_frame
    setting_frame.pack()


def change_setting_adr(setting_dir,str_dir):

    def change_schedule(adr):
        root.schedule_adr=adr
        setting_dir["root.schedule_adr"]=adr
    
    def change_library(adr):
        root.library_adr=adr
        setting_dir["root.library_adr"]=adr

    def change_logs(adr):
        root.logs_adr=adr
        setting_dir["root.logs_adr"]=adr

    def change_setting(adr):
        root.setting_adr=adr
        setting_dir["root.setting_ad"]=adr

    change_all_dir = {"1": change_schedule, "2": change_library, "3": change_logs,"4":change_setting}
    count=1
    for _ in str_dir:
        if _:
            change_all_dir[str(count)](_)
        count = count + 1
    with open("setting.json",mode="w",encoding="utf-8") as f:
            f.write(json.dumps(setting_dir, sort_keys=True, indent=4, separators=(',', ': ')))


def show_in_txt(text,data):
    text.delete(1.0, "end")
    text.insert("end",data)
    return text


if __name__ == '__main__':
    root = basedesk()
    now_frame=tk.Frame(root.root)

    main_screen()

    root.root.mainloop()