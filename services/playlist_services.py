import pymysql as pms

host = 'localhost'
user='root'
password='root'
charset='utf8mb4'
connection = pms.connect(host=host, user=user, password=password, charset=charset, db='mydb')


def get_playlist_info(uid,pid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT playlist_title,(select name from user where uid=creator),creator FROM playlist WHERE pid=%s"
            cursor.execute(sql,pid)
            playlist_title, creator,creator_uid = cursor.fetchone()

            sql = "SELECT vid, uid, video_title, name, creation_time FROM user,has_video,video WHERE uid=uploader AND vid=video_vid AND playlist_pid=%s"
            cursor.execute(sql,pid)
            playlist_video_info = cursor.fetchall()
            
        connection.commit()
        return playlist_title, creator, creator_uid, playlist_video_info
    
    except Exception as e:
        print(">>",e)
        return "No Title","No Creator", []

def add_to_my_playlist(uid,pid):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO has_playlist(user_uid, playlist_pid) VALUES(%s,%s)"
            cursor.execute(sql,(uid,pid))
        
        connection.commit()
        return 1
    
    except:
        return 0

def delete_playlist(pid):
    with connection.cursor() as cursor:
        sql = "DELETE FROM playlist WHERE pid=%s"
        cursor.execute(sql,pid)
    connection.commit()