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
            

def mainloop(s:str):
    if s=="exit":
        return s
    ss=s.split(" ")
    if len(ss)>0:
        if ss[0]=="cd":
            if len(ss)>1:
                os.chdir(ss[1])
                return ""
        if ss[0]=="pwd":
            return str(os.curdir())
        else:
            return "!"
    return ""



starts(":>",mainloop)
