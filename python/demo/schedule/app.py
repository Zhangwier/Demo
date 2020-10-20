import tkinter as tk
import time
import shutil,os
import json
import multiprocessing


#封装成app!
class Schedule_app():

    def __init__(self,setting_file_adr=""):

        #系统初始化-------------------------------------------------

        self.root = tk.Tk()
        self.root.title('My assistant')
        self.root.geometry('600x400')
        self.root.minsize(600, 400) #最小尺寸
        self.root.maxsize(600, 400) #最大尺寸
        #读取设置文件------------------------------------------------
        try:
            self.setting_dir=json.load("setting.json")
        except:
            #设置文件创建
            if not os.path.exists("logs"):
                os.mkdir("logs")
            if not os.path.exists("library"):
                os.mkdir("library")
            self.setting_dir={}
            self.setting_dir["setting_adr"] = "setting.json" # 设置地址 json
            self.setting_dir["logs_adr"] = "logs" # 日志地址 文件
            self.setting_dir["library_adr"] = "library" # 库地址 文件
            self.setting_dir["direction_list"] = [] #方向列表 方向 = {[路径节点:地址,状态]}
            self.setting_dir["plan_dir"] = {} # 计划字典 {计划:(时间|次序,地址)}
            self.setting_dir["command_list"] = [] # 指令集 [序列:地址,时间:地址]
            self.setting_dir["server_setting"] = {} # 服务器设置
            self.setting_dir["memory_dir"] = {} # 记忆

            #设置文件写入
            with open("setting.json",mode="w",encoding="utf-8") as f:
                f.write(json.dumps(self.setting_dir,\
                    sort_keys=True, indent=4, separators=(',', ': ')))

        #临时变量------------------------------------------------------
        self.screen_list = [] #需要放置(主要是为了摧毁)的所有界面
    
    # return data_str or dir
    def load_file(self,file_adr):

        def Ctxt():
            data = {}
            with open(file_adr, mode="r", encoding="utf-8") as f:
                return f.read()

        def Cjson():
            return json.load(file_adr)

        def Csql():
            return "We havent update the file"
            
        # 格式判断
        if os.path.isdir(file_adr): # 目录
            return os.listdir(file_adr)
        elif not os.path.isfile(file_adr): # 啥也不是 | 怎么可能?
            return("Error!Enter a filename with a formatted suffix." + "\n" + file_adr)
        else:
            try:
                format_load_dir = {"txt": Ctxt, "json": Cjson, "sql": Csql}
                return format_load_dir[file_adr.split(".")[-1]]()
            except:
                return "Unreadable file format\nWe load in txt\n\n" + Ctxt()

    def save_file_data(self,file_adr,save_data):

        def Ctxt():
            data = {}
            with open(file_adr, mode="w", encoding="utf-8") as f:
                f.write(save_data)

        def Cjson():
            with open("setting.json",mode="w",encoding="utf-8") as f:
                f.write(json.dumps(save_data, sort_keys=True, indent=4, separators=(',', ': ')))

        def Csql():
            return "We havent update the file"

        if os.path.isdir(file_adr): # 目录
            pass
            #return os.listdir(file_adr)
        else:
            try:
                format_load_dir = {"txt": Ctxt, "json": Cjson, "sql": Csql}
                return format_load_dir[file_adr.split(".")[-1]]()
            except:
                Ctxt()

    # command-----------------------------------------
    def show_in_txt(self,Text,data):
        Text.delete(1.0, "end")
        Text.insert("end",data)
        return Text

    def change_setting_adr(self,str_dir):

        def change_memory(adr):
            self.setting_dir["memory_dir"]=adr
            # pass
    
        def change_library(adr):
            old_adr,self.setting_dir["library_adr"] = self.setting_dir["library_adr"],adr
            shutil.move(old_adr,adr)

        def change_logs(adr):
            old_adr,self.setting_dir["logs_adr"] = self.setting_dir["logs_adr"],adr
            shutil.move(old_adr,adr)

        def change_setting(adr):
            os.remove(self.setting_dir["setting_adr"])
            self.setting_dir["setting_adr"] = adr

        change_all_dir = {"1": change_memory, "2": change_library, "3": change_logs,"4":change_setting}
        count=1
        for _ in str_dir:
            if _:
                change_all_dir[str(count)](_)
            count = count + 1
        with open(self.setting_dir["setting_adr"],mode="w") as f:
                f.write(json.dumps(self.setting_dir, sort_keys=True, indent=4, separators=(',', ': ')))
    
    # screen -------------------------------------------
    def screen(self):

        # 模板-------------------
        def file_choise_screen(screen,file_list):
            #file_name = tk.StringVar()
            file_dir = tk.Listbox(screen) # 空列表
            for _ in file_list:
                file_dir.insert('end', _)
            choised_file = file_dir.get(file_dir.curselection()) # 选中的文件

            open_library_botton = tk.Button(screen,text='open',\
                command=lambda:self.show_in_txt(screen,data=self.load_file(self.setting_dir["library_adr"])),width=10, height=1)

        def main_screen():
            main_frame = tk.Frame(master=self.root)
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
            #图片
            #image_file = tk.PhotoImage(file='pic.gif')
            #image = canvas.create_image(200, 0, anchor='n',image=image_file)

            #按键放置
            canvas.pack(side=tk.TOP,pady=6)
            schedule_button.pack(side=tk.TOP,pady=6)
            library_button.pack(side=tk.TOP,pady=6)
            logs_button.pack(side=tk.TOP,pady=6)
            setting_button.pack(side=tk.TOP,pady=6)
            
            for _ in self.screen_list:
                _.destroy()
            self.screen_list = [main_frame]
            #界面pack
            main_frame.pack()

        def schedule_screen():

            if not self.setting_dir["direction_list"] :
                pass
            
            schedule_frame = tk.Frame(master=self.root)
            back_botton = tk.Button(schedule_frame,text='BACK',\
                command=main_screen,width=10, height=1)

            back_botton.pack(anchor=tk.S, side=tk.RIGHT,padx=10, pady=10)

            for _ in self.screen_list:
                _.destroy()
            self.screen_list = [schedule_frame]
            schedule_frame.pack()

        def library_screen():
            library_frame = tk.Frame(master=self.root)
            open_library_botton = tk.Button(library_frame,text='open',\
                command=lambda:self.show_in_txt(Text=library_show,\
                    data=self.load_file(self.setting_dir["library_adr"] + "\\" + \
                        library_file_dir.get(library_file_dir.curselection()))),width=10, height=1)
            save_library_botton = tk.Button(library_frame,text='save',\
                command=lambda:self.save_file_data(self.setting_dir["library_adr"] + "\\" + \
                        library_file_dir.get(library_file_dir.curselection()),library_show.get("end")),width=10, height=1)
            back_botton = tk.Button(library_frame,text='BACK',\
                command=main_screen,width=10, height=1)
            library_file_dir = tk.Listbox(library_frame,width=15,height=20)
            for _ in self.load_file(self.setting_dir["library_adr"]):
                library_file_dir.insert('end', _)
            library_show = tk.Text(library_frame,width=40, height=20)

            library_file_dir.pack(side=tk.LEFT,padx=1, pady=5)
            library_show.pack(side=tk.TOP,padx=5, pady=5)
            open_library_botton.pack(side=tk.LEFT,padx=5, pady=5)
            save_library_botton.pack(side=tk.LEFT,padx=5, pady=5)
            back_botton.pack(side=tk.LEFT,padx=5, pady=5)

            for _ in self.screen_list:
                _.destroy()
            self.screen_list = [library_frame]
            library_frame.pack()

        def logs_screen():
            logs_frame = tk.Frame(master=self.root)
            back_botton = tk.Button(logs_frame,text='BACK',\
                command=main_screen,width=10, height=1)
            logs_file_dir = tk.Listbox(logs_frame,width=15,height=20)
            for _ in self.load_file(self.setting_dir["logs_adr"]):
                logs_file_dir.insert('end', _)
            logs_show = tk.Text(logs_frame,width=40, height=20)
            open_library_botton = tk.Button(logs_frame,text='open',\
                command=lambda:self.show_in_txt(logs_show,\
                    data=self.load_file(self.setting_dir["logs_adr"] + "\\" + \
                        logs_file_dir.get(logs_file_dir.curselection()))),width=10, height=1)
            save_logs_botton = tk.Button(logs_frame,text='save',\
                command=lambda:self.save_file_data(self.setting_dir["logs_adr"] + "\\" + \
                        logs_file_dir.get(logs_file_dir.curselection()),logs_file_dir.get("end")),width=10, height=1)

            logs_file_dir.pack(side=tk.LEFT,padx=5, pady=5)
            logs_show.pack(side=tk.TOP,padx=5, pady=5)
            open_library_botton.pack(side=tk.LEFT,padx=5, pady=5)
            save_logs_botton.pack(side=tk.LEFT,padx=5, pady=5)
            back_botton.pack(anchor=tk.S, side=tk.LEFT,padx=5, pady=5)

            for _ in self.screen_list:
                _.destroy()
            self.screen_list = [logs_frame]
            logs_frame.pack()

        def setting_screen():
            
            setting_frame = tk.Frame(master=self.root)
            change_schedule_botton = tk.Button(setting_frame,text='change',\
                command=main_screen,width=10, height=1)
            change_all_label = tk.Label(setting_frame, text=\
                'Memory address\n\n\nLibrary address\n\n\nLogs address\n\n\nSetting address', \
                width=15, height=13)
            change_memory_entry = tk.Entry(setting_frame,width=20)
            change_library_entry = tk.Entry(setting_frame,width=20)
            change_logs_entry = tk.Entry(setting_frame,width=20)
            change_setting_entry = tk.Entry(setting_frame,width=20)
            change_all_botton = tk.Button(setting_frame,text='change',\
                command=lambda:self.change_setting_adr([change_memory_entry.get(),\
                    change_library_entry.get(),\
                        change_logs_entry.get(),\
                            change_setting_entry.get()\
                                ]),width=10, height=1)
            back_botton = tk.Button(setting_frame,text='BACK',\
                command=main_screen,width=10, height=1)

            change_all_label.pack(anchor=tk.N, side=tk.LEFT,padx=0, pady=2)
            change_memory_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=30)
            change_library_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=13)
            change_logs_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=20)
            change_setting_entry.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=20)
            change_all_botton.pack(anchor=tk.N, side=tk.TOP,padx=10, pady=15)
            back_botton.pack(anchor=tk.S, side=tk.BOTTOM,padx=2, pady=2)

            for _ in self.screen_list:
                _.destroy()
            self.screen_list = [setting_frame]
            setting_frame.pack()

        def aitalk_screen():
            aitalk_frame = tk.Frame(master=self.root)
            back_botton = tk.Button(aitalk_frame,text='BACK',\
                command=main_screen,width=10, height=1)

            back_botton.pack(anchor=tk.S, side=tk.RIGHT,padx=10, pady=10)
        
            for _ in self.screen_list:
                _.destroy()
            self.screen_list = [aitalk_frame]
            aitalk_frame.pack()
        
        def error_screen():
            error_screen = tk.messagebox.showerror(title='error', message='error！')
            #tk.messagebox.showinfo(title='Hi', message='你好！')              # 提示信息对话窗
            #tk.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
            #tk.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
            # print(tk.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
            # print(tk.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
            # print(tk.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'

        
        main_screen()
        self.screen_list.append(tk.Frame(master=self.root)) # 防止bug

    def start(self):

        #界面初始化----------------------------------------------------
        self.screen()
        self.root.mainloop()

    # 向服务器发送数据
    def send_massage(self,data):
        pass

    # 接收数据
    def accept_massage(self):
        data=""
        return data


if __name__ == '__main__':
    app =  Schedule_app()
    app.start()
