#CopyFile.py


def CopyFile(file1,file2=""):
    if not file2:
        file2=file1.split(".")[0]+"-副本."+file1.splito(".")[1]
    lines=[]
    with open (file1,mode="r",encoding="utf-8") as f:
        for _ in f.readlines():
            lines.append(_)
    if lines:
    	print("读取失败 or 文件为空")
    	return 0
    with open(file2,mode="w",encoding="utf-8") as f:
        for _ in lines:
            f.writelines(_)


def main():
    FileName="C:\\Users\\考拉\\Documents\\_JB\\python\\library.txt"
    OldFileName="C:\\Users\\考拉\\Documents\\_JB\\python\\src\\library- 副本.txt"
    try:
        CopyFile(OldFileName,FileName)
    except:
        print("error in FileName")


if __name__ == '__main__':
    main()