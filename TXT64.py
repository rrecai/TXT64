text = ""
print("TEXT EDITOR BEGIN")
def txexit(x):
    print("TEXT EDITOR END")
    exit(x)
while True:
    x = input()
    if(x=="TEXT EDITOR WRITEQUIT" or x=="TEXT EDITOR WRITE"):
        y=input("FILENAME: ")
        try:
            f = open(y,"x")
            f.write(text)
            txexit(0) if x=="TEXT EDITOR WRITEQUIT" else None
        except Exception as e:
            if isinstance(e==FileExistsError):
                if input("FILENAME EXISTS, CONTINUE?: ").lower=="yes":
                    f=open(y,"w")
                    f.write(text)
                    txexit(0) if x=="TEXT EDITOR WRITEQUIT" else None
            else:
                print("ERROR:\n",e)
                txexit(1)
    elif(x=="TEXT EDITOR OPEN"):
        try:
            f = open(input("FILENAME: "),"r+")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNEW SESSION\n--------------------------")
            print(f.read())
            text=f.read()
        except Exception as e:
            if isinstance(e==FileNotFoundError):
                print("NOT FOUND")
            else:
                print(e)
                txexit(1)
    elif(x=="TEXT EDITOR QUIT"):
        txexit(0)
    elif(x=="TEXT EDITOR HELP"):
        print("WRITE\tWRITEQUIT\tOPEN\tQUIT\tHELP")
    else:
        text+=("\n"+x)
