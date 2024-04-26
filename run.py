import sys, subprocess, os
def update():
    subprocess.call("rmdir /S /Q dbc", shell=True)
    subprocess.run(['git', 'clone', 'https://gitlab.com/prokne/bradavice-online-dbc.git', 'dbc'])
def convertToCsv(dbc=None):
    if dbc:
        os.remove(f"dbc/{dbc}.dbc.csv") if os.path.exists(f"dbc/{dbc}.dbc.csv") else None
        subprocess.run(['DBCUtil.exe', f"dbc\{dbc}.dbc"])
    else:
        for dirName, subdirList, fileList in os.walk("dbc"):
            for f in fileList:
                if f.endswith(".csv"):
                    os.remove(f"dbc/{f}")
            for f in fileList:
                if f.endswith(".dbc"):
                    subprocess.run(['DBCUtil.exe', f"dbc\{f}"])
def convertToDbc(dbc=None):
    if dbc:
        os.remove(f"dbc/{dbc}.dbc") if os.path.exists(f"dbc/{dbc}.dbc") else None
        subprocess.run(['DBCUtil.exe', f"dbc\{dbc}.dbc.csv"])
    else:
        for dirName, subdirList, fileList in os.walk("dbc"):
            for f in fileList:
                if f.endswith(".dbc"):
                    os.remove(f"dbc/{f}")
            for f in fileList:        
                if f.endswith(".csv"):
                    subprocess.run(['DBCUtil.exe', f"dbc\{f}"])
def push():
    os.chdir("dbc")
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', '"converterAutoUpdate"'])
    subprocess.run(['git', 'push'])
def convert():
    convertToDbc()
    for dirName, subdirList, fileList in os.walk("dbc"):
        for f in fileList:
            if f.endswith(".csv"):
                os.remove(f"dbc/{f}")
    push()

if __name__ == '__main__':
    if len(sys.argv) < 2: convert()
    elif sys.argv[1] == "update": update()
    elif sys.argv[1] == "csv": convertToCsv(sys.argv[2] if len(sys.argv) >= 3 else None)
    elif sys.argv[1] == "dbc": convertToDbc(sys.argv[2] if len(sys.argv) >= 3 else None)
    else: print("Error in Arguments!")