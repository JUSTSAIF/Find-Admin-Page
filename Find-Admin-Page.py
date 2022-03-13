from urllib import request
import json,threading
TC = threading.Condition()
paths =  json.loads(request.urlopen('https://pastebin.com/raw/iUC5f20Z').read())
FoundsPaths = []
Count = 0

def check(url,path):
    global Count
    try:
        request.urlopen(url)
        FoundsPaths.append(path)
    except:
        pass
    TC.acquire()
    Count += 1
    print("\033[H\033[J")
    print("    ===========================")
    print("    -=   Admin Page Finder   =-")
    print("    ===========================")
    print(F"    [!] Checking Path >> {path}")
    print(F"    [!] Count >> {str(Count)}/{str(len(paths))}")
    print(F"    [+] Paths Found >> {str(len(FoundsPaths))}")
    print("    ===========================")
    if Count == len(paths):
        if len(FoundsPaths) == 0:
            print("    [!] No Path Found")
        else:
            print(F"    - Paths Found :")
            for path in FoundsPaths:
                print(F"    - /{path}")
        print("    [+] Done")
    TC.notify_all()
    TC.release()



print("""\n\n
    ===========================
    -=   Admin Page Finder   =-
    ===========================\n\n
""")
url=input("    [!] WEBSITE >> ")
for path in paths:
    URL = F"{url}/{path}"
    threading.Thread(target=check,args=(URL,path)).start()