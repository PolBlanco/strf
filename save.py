import hashlib
import os
carpeta = os.path.join(os.path.dirname(__file__),'.saves','.wt.save')
carpeta1 = os.path.join(os.path.dirname(__file__),'.saves','.chk.sum')
def save(time,level,px,py,heal,selection):
    try:
        f = open(carpeta, "w")
        f.write(f"{int(time)}\n")
        f.write(f"{int(level)}\n")
        f.write(f"{int(px[0])}\n")
        f.write(f"{int(px[1])}\n")
        f.write(f"{int(py[0])}\n")
        f.write(f"{int(py[1])}\n")
        f.write(f"{int(heal[0])}\n")
        f.write(f"{int(heal[1])}\n")
        f.write(f"{int(selection[0])}\n")
        f.write(f"{int(selection[1])}\n")
        f.close()
        r = open(carpeta, "r")
        readed = r.read()
        h = open(carpeta1, "w")
        h.write(hashlib.md5(readed.encode(encoding="UTF-8",errors="replace")).hexdigest())
        #print("read", readed)
        #print(hashlib.md5(readed.encode('utf-8')).hexdigest())
        r.close()
        h.close()
    except Exception as err:
        print(err)
        a = open(carpeta, "a")
        h = open(carpeta1, "a")
        a.close()
        h.close()

carpeta = os.path.join(os.path.dirname(__file__),'.saves','.wt.save')
carpeta1 = os.path.join(os.path.dirname(__file__),'.saves','.chk.sum')
def load():
    try:
        f = open(carpeta, "r")
        time = int(f.readline()[:-1])
        level = int(f.readline()[:-1])
        px = [int(f.readline()[:-1]), int(f.readline()[:-1])]
        py = [int(f.readline()[:-1]),int(f.readline()[:-1])]
        heal = [int(f.readline()[:-1]),int(f.readline()[:-1])]
        selection = [int(f.readline()[:-1]),int(f.readline()[:-1])]
        f.close()
        h = open(carpeta1, "r")
        hread = h.read()
        r = open(carpeta, "r")
        read = r.read()
        if hread == hashlib.md5(read.encode('utf-8')).hexdigest():
            r.close()
            h.close()
            return time, level, px, py, heal, selection
        else:
            print("Antihack does it very well ;)")
            r.close()
            h.close()
            return 0, 0, 0, 0, 0, [0, 0]
    except Exception as err:
        print(err)
        return 0, 0, 0, 0, 0, [0, 0]
#Prueba