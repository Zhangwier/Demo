#sort all my library
#-------------------
#SortScript.py


def sort_txt(adr):
	lins=[]
	with open (adr,"r",encoding="utf-8") as f:
	    for _ in f.readlines():
	        lins.append(_)
	    lins.sort()
	with open (adr,"w",encoding="utf-8") as f:
	    for _ in lins:
		    f.writelines(_)


def main():
    adr="C:\\Users\\考拉\\Documents\\_JB\\python"
    FileName="library.txt"
    sort_txt(adr+FileName)


if __name__ == "__main__":
	main()


