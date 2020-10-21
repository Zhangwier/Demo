import json
import pymysql
from functools import wraps


#可改动的设置
class Setting():
    def __init__(self):
        # 能读取的格式,暂时没起到应有的作用....
        self.format_dir = ("txt", "json")
        # ---------------------------------------------------
        # 使用format_dir生成format_load_dir和format_change_dir
        # 采用单例模式


# 日志记录器
def logs(fn):
    @wraps(fn)
    def write_logs(*args,**kwargs):
        with open("logs.txt","w") as f:
    	    try:
    	    	fn(*args,**kwargs)
    	    	f.write(str(fn)+":success")
    	    except:
    	    	f.write(str(fn)+":error")
    return write_logs


# 读入数据
def load_data(setting,file_name):

    def formatting_file_name(file_name):
        if not file_name.split(".")[-1]:
            TxtPrint("Error!Enter a filename with a formatted suffix.")
        elif file_name.split(".")[-1] not in setting.format_dir:
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


# 转换并保存
def change_data(setting,data,goal_format,file_name):

    def Clear_file_name(file_name):
        return file_name.split(".")[0]

    def Ctxt(data, file_name):
        file_name = file_name+".txt"
        with open(file_name, mode="w") as f:
            f.write(data)

    def Cjson(data, file_name):
        file_name = file_name+".json"
        with open(file_name, mode="w") as f:
            f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

    def Csql(data, file_name):
        pass

    format_change_dir = {"txt": Ctxt, "json": Cjson, "sql": Csql}
    file_name=Clear_file_name(file_name)
    format_change_dir[goal_format](data,file_name)


# 文本显示
def TxtPrint(txt):
    print(txt)


def main():
    setting = Setting()
    TxtPrint("请输入文件名")
    file_name = input()
    TxtPrint("请输入想转换格式")
    goal_format= input()
    data = load_data(setting,file_name)
    change_data(setting,data, goal_format, file_name)


if __name__ == "__main__":
    main()
