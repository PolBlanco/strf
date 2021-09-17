import hashlib
import os
def gen_hash():
    try:
        f1 = open(f'{os.path.dirname(__file__)}/main.py', "r")
        f2 = open(f'{os.path.dirname(__file__)}/save.py', "r")
        f3 = open(f'{os.path.dirname(__file__)}/online.py', "r")
        f4 = open(f'{os.path.dirname(__file__)}/server_init.py', "r")
        f5 = open(f'{os.path.dirname(__file__)}/server-installation.py', "r")
        f6 = open(f'{os.path.dirname(__file__)}/server-installation.sql', "r")
        f7 = open(f'{os.path.dirname(__file__)}/CHARACTERS.py', "r")
        f8 = open(f'{os.path.dirname(__file__)}/anticheat.py', "r")
        files = f1.read() + f2.read() + f3.read() + f4.read() + f5.read() + f6.read() + f7.read() + f8.read()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
        f7.close()
        f8.close()
        h = open(f'{os.path.dirname(__file__)}/.chk.sum', "w")
        h.write(hashlib.md5(files.encode('utf-8')).hexdigest())
        #print("read", readed)
        #print(hashlib.md5(readed.encode('utf-8')).hexdigest())
        h.close()
    except Exception as err:
        print(err)
        h = open(f'{os.path.dirname(__file__)}/.chk.sum', "a")
        h.close()


def load_hash():
    try:
        f1 = open(f'{os.path.dirname(__file__)}/main.py', "r")
        f2 = open(f'{os.path.dirname(__file__)}/save.py', "r")
        f3 = open(f'{os.path.dirname(__file__)}/online.py', "r")
        f4 = open(f'{os.path.dirname(__file__)}/server_init.py', "r")
        f5 = open(f'{os.path.dirname(__file__)}/server-installation.py', "r")
        f6 = open(f'{os.path.dirname(__file__)}/server-installation.sql', "r")
        f7 = open(f'{os.path.dirname(__file__)}/CHARACTERS.py', "r")
        f8 = open(f'{os.path.dirname(__file__)}/anticheat.py', "r")
        files = f1.read() + f2.read() + f3.read() + f4.read() + f5.read() + f6.read() + f7.read() + f8.read()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        f5.close()
        f6.close()
        f7.close()
        f8.close()
        h = open(f'{os.path.dirname(__file__)}/.chk.sum', "r")
        hread = h.read()
        if hread == hashlib.md5(files.encode('utf-8')).hexdigest():
            h.close()
            return True
        else:
            print("Antihack does it very well ;)")
            h.close()
            return False
    except Exception as err:
        print(err)
        return False