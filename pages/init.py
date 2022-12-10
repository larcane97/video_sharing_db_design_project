
from services.init_services import check_account,create_account
from pages.main import user_main_page,admin_main_page

def init_page():
    while True:
        print("-"*100)
        print("[LOGIN PAGE]")
        print("0. Exit")
        print("1. login to user")
        print("2. login to admin")
        print("3. create user account")
        print("4. create admin account")

        print("Input:",end=" ")
        command = int(input())

        if command==0:
            return -1
        elif command==1 or command==2:
            print("id :",end=" ")
            id = input()
            print("password :",end=" ")
            password = input()

            uid = check_account(id,password,True if command==2 else False)
            if uid:
                print("login success.")
                if command==1:
                    user_main_page(uid)
                else:
                    admin_main_page(uid)
            else:
                print("Wrong either id or password.")

        elif command==3 or command==4:
            print("id :",end=" ")
            id = input()
            print("password :",end=" ")
            password = input()
            print("name :",end=" ")
            name = input()
            print("email :",end=" ")
            email = input()

            uid = create_account(id,password,name,email,True if command==4 else False)

            if uid:
                print("create account success.")
                if command==3:
                    user_main_page(uid)
                else:
                    admin_main_page(uid)
            else:
                print("Can't create account. check either id or email duplication")

        else:
            print("Wrong command.")