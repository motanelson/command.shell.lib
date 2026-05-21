import cmd
import os




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



cmd.starts(":>",mainloop)

