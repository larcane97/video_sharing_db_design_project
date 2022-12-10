from services.account_info_change_services import change_password,change_email,change_name


def account_info_change_page(uid):
    while True:
        print("-"*100)
        print("[ACCOUNT INFO CHANGE PAGE]")
        print("0. return to previous page")
        print("1. change password")
        print("2. change name")
        print("3. change email")
        
        print("Input: ",end="")
        command = int(input())
        
        if command==0:
            break
        elif command == 1:
            print("new password : ",end="")
            password = input()
            if change_password(uid,password):
                print("success changing password.")
            else:
                print("fail changing password.")

        elif command==2:
            print("new name : ",end="")
            name = input()
            if change_name(uid,name):
                print("success changing name.")
            else:
                print("fail changing name.")

        elif command==3:
            print("new email : ",end="")
            email = input()
            if change_email(uid,email):
                print("success changing email.")
            else:
                print("fail changing email.")