import pymysql as pms

host = 'localhost'
user='root'
password='root'
charset='utf8mb4'
connection = pms.connect(host=host, user=user, password=password, charset=charset, db='mydb')

def check_account(id,password,admin_check):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT uid FROM USER WHERE id=%s AND password=%s"
            cursor.execute(sql,(id,password))
            uid = cursor.fetchone()[0]
            connection.commit()

            if uid and admin_check:
                    cursor.execute("SELECT user_uid FROM ADMIN WHERE user_uid=%s",(uid,))
                    is_admin = cursor.fetchone()[0]

        if uid and not admin_check:
            return uid
        if uid and admin_check and is_admin:
            return uid
        return 0
    except:
        return 0

def create_account(id,password,name,email,is_admin):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO USER(id,password,name,email) VALUES(%s,%s,%s,%s)"
            cursor.execute(sql,(id,password,name,email))

            cursor.execute("select last_insert_id() from user;")
            uid = cursor.fetchone()[0]

            if is_admin:
                sql = "INSERT INTO ADMIN(user_uid) VALUES(%s)"
                cursor.execute(sql,(uid,))

        connection.commit()
        return uid
    except Exception as e:
        return 0



