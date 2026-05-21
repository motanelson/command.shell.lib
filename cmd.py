import os





def starts(promth:str,mainloops):
    while 1:
        print(promth,end=" ")
        a=input().strip()
        b=mainloops(a)
        if b=="exit":
            break
        if b=="!":
            os.system(a)
        else:
            print(b)
            

