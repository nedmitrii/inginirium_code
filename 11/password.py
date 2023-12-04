password = "password"

def ask_password():
    for i in range(3):
        p = input("Введите пароль")
        if p == password:
            print("принят")
            return
    print("В доступе отказано")

ask_password()