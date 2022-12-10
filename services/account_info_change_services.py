import pymysql as pms

host = 'localhost'
user='root'
password='root'
charset='utf8mb4'
connection = pms.connect(host=host, user=user, password=password, charset=charset, db='mydb')

def change_password(uid,password):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE USER SET password=%s WHERE uid=%s;"
            cursor.execute(sql,(password,uid))

        connection.commit()
        return 1
    except:
        return 0

def change_name(uid,name):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE USER SET name=%s WHERE uid=%s;"
            cursor.execute(sql,(name,uid))

        connection.commit()
        return 1
    except:
        return 0

def change_email(uid,email):
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE USER SET email=%s WHERE uid=%s;"
            cursor.execute(sql,(email,uid))

        connection.commit()
        return 1
    except:
        return 0