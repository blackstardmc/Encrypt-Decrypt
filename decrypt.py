from cryptography.fernet import Fernet
import os


def returnKey():
    return open("key.key", 'rb').read()


def decrypt(items, key):
    i = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        data = i.decrypt(file_data)

        with open(item, 'wb') as file:
            file.write(data)


if __name__ == '__main__':
    #Lugar donde va a desencriptar
    path = "C:\\Users\\BlackStar\\Desktop\\Nueva carpeta (2)"
    os.remove(path+"\\"+"Readme.txt")
    items = os.listdir(path)
    directories = [path + "\\" + x for x in items]




key = returnKey()
decrypt(directories, key)
