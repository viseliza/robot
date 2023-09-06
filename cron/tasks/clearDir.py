import os
from datetime import datetime

#
# TODO: Снести и пареписать
#
def clearDir():
    # 
    dn = datetime.now() 
    
    # Создаём папку, если нету
    if not os.path.exists("./tmp"): return False
    print(dn)
    for file in os.listdir("./tmp"):
        if int(file.split(".")[2]) < dn.year \
            or int(file.split(".")[1]) < dn.month \
            or int(file.split(".")[0]) < dn.day:
            os.remove(f"tmp/{file}")
