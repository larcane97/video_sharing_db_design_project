import pymysql as pms
from pymysql.constants import CLIENT

host = 'localhost'
user='root'
password='root'
charset='utf8mb4'
connection = pms.connect(host=host, user=user, password=password, charset=charset, db='mydb',client_flag=CLIENT.MULTI_STATEMENTS)

def account_delete(uid,password):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT password FROM USER WHERE uid=%s"
            cursor.execute(sql,(uid,))
            org_password = cursor.fetchone()[0]
            
            if password == org_password:
                sql = "DELETE FROM USER WHERE uid=%s"
                cursor.execute(sql,(uid,))
            else:
                return 0

        connection.commit()
        return 1
    except:
        return 0

def search_playlist(playlist_title,is_admin=False):
    try:
        with connection.cursor() as cursor:
            if is_admin:
                sql = "SELECT pid,playlist_title FROM playlist WHERE playlist_title LIKE %s"
            else:    
                sql = "SELECT pid,playlist_title FROM playlist WHERE is_playlist_public=1 AND playlist_title LIKE %s"
            cursor.execute(sql,(f"%{playlist_title}%",))
            playlist_list = cursor.fetchall()

        if len(playlist_list)==0:
            return 0
            
        print("result")
        for idx, (_,playlist) in enumerate(playlist_list):
            print(f"\t{idx+1}. playlist title : {playlist}")
        print()
        print("\tselect the playlist number that you want to search(enter 0 to return)")
        print("\tnumber : ",end="")
        playlist_num = int(input())

        if playlist_num==0:
            return 0
        pid = playlist_list[playlist_num-1][0]

        connection.commit()
        return pid
    
    except Exception as e:
        print(">>",e)
        return 0  

def search_video(video_title,is_admin=False):
    try:
        with connection.cursor() as cursor:
            if is_admin:
                sql = "SELECT vid,video_title FROM video WHERE video_title LIKE %s"
            else:
                sql = "SELECT vid,video_title FROM video WHERE is_video_public=1 AND video_title LIKE %s"
            cursor.execute(sql,(f"%{video_title.strip()}%",))
            video_list = cursor.fetchall()
        print(">>",is_admin)
        if len(video_list)==0:
            return 0
            
        print("result")
        for idx, (_,video) in enumerate(video_list):
            print(f"\t{idx+1}. video title : {video}")
        print()
        print("\tselect the video number that you want to search(enter 0 to return)")
        print("\tnumber : ",end="")
        video_num = int(input())

        if video_num==0:
            return 0
        vid = video_list[video_num-1][0]

        connection.commit()
        return vid
    
    except Exception as e:
        print(">>",e)
        return 0  

def search_user(user_name):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT uid,name FROM USER WHERE name LIKE %s"
            cursor.execute(sql,(f"%{user_name}%",))
            user_list = cursor.fetchall()

        if len(user_list)==0:
            return 0
            
        print("search result")
        for idx, (_,user) in enumerate(user_list):
            print(f"\t{idx+1}. user name : {user}")
        print()
        print("\tselect the user number that you want to search(enter 0 to return)")
        print("\tnumber : ",end="")
        user_num = int(input())

        if user_num==0:
            return 0
        uid = user_list[user_num-1][0]

        connection.commit()
        return uid
    
    except:
        return 0

def show_upload_video(uid,search_uid):
    try:
        with connection.cursor() as cursor:
            if uid==search_uid: # 비공개 영상도 모두 보이도록
                sql = "SELECT vid, video_title FROM video WHERE uploader=%s"
            else:
                sql = "SELECT vid, video_title FROM video WHERE uploader=%s AND is_video_public=1"
            
            cursor.execute(sql,(search_uid,))
            video_list = cursor.fetchall()

            if len(video_list)==0:
                return 0
                
            print("search result")
            for idx, (_,title) in enumerate(video_list):
                print(f"\t{idx+1}. video title : {title}")
            print()
            print("\tselect the video number that you want to watch(enter 0 to return)")
            print("\tnumber : ",end="")
            video_num = int(input())

            if video_num==0:
                return 0

            vid = video_list[video_num-1][0]
        connection.commit()
        return vid
    except Exception as e:
        return 0

def show_playlist(uid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT pid,playlist_title FROM has_playlist,playlist WHERE user_uid=%s and playlist_pid=pid"
            
            cursor.execute(sql,(uid,))
            playlists = cursor.fetchall()

            if len(playlists)==0:
                return 0
                
            print("search result")
            for idx, (_,playlist_title) in enumerate(playlists):
                print(f"\t{idx+1}. playlist title : {playlist_title}")
            print()
            print("\tselect the palylist number that you want to watch(enter 0 to return)")
            print("\tnumber : ",end="")
            playlist_num = int(input())

            if playlist_num==0:
                return 0

            pid = playlists[playlist_num-1][0]
        connection.commit()
        return pid
    except Exception as e:
        print(">>",e)
        return 0

def show_like_videos(uid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT vid, video_title FROM watched, video WHERE vid=video_vid and user_uid=%s and is_like=1;"
            
            cursor.execute(sql,(uid,))
            like_videos = cursor.fetchall()

            if len(like_videos)==0:
                return 0
                
            print("search result")
            for idx, (_,video) in enumerate(like_videos):
                print(f"\t{idx+1}. video title : {video}")
            print()
            print("\tselect the video number that you want to watch(enter 0 to return)")
            print("\tnumber : ",end="")
            video_num = int(input())

            if video_num==0:
                return 0

            vid = like_videos[video_num-1][0]
        connection.commit()
        return vid
    except:
        return 0

def show_commented_videos(uid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT video_vid,content,write_time FROM user,watched,comment WHERE uid=user_uid AND video_vid=watched_video_vid AND user_uid=watched_user_uid AND uid=%s;"
            
            cursor.execute(sql,(uid,))
            commented_videos = cursor.fetchall()

            if len(commented_videos)==0:
                return 0
                
            print("search result")
            for idx, (vid, content, write_time) in enumerate(commented_videos):
                cursor.execute("SELECT video_title FROM video WHERE vid=%s",(vid))
                video_title = cursor.fetchone()[0]
                print(f"\t{idx+1}. video title : {video_title}, comment : {content}, write_time : {write_time}")
            print()
            print("\tselect the video number that you want to watch(enter 0 to return)")
            print("\tnumber : ",end="")
            video_num = int(input())

            if video_num==0:
                return 0

            vid = commented_videos[video_num-1][0]
        connection.commit()
        return vid
    except:
        return 0

def show_watched_videos(uid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT vid, video_title FROM watched, video WHERE user_uid=%s and vid=video_vid;"
            
            cursor.execute(sql,(uid,))
            watched_videos = cursor.fetchall()

            if len(watched_videos)==0:
                return 0
                
            print("search result")
            for idx, (_, video_title) in enumerate(watched_videos):
                print(f"\t{idx+1}. video title : {video_title}")
            print()
            print("\tselect the video number that you want to watch(enter 0 to return)")
            print("\tnumber : ",end="")
            video_num = int(input())

            if video_num==0:
                return 0

            vid = watched_videos[video_num-1][0]
        connection.commit()
        return vid
    except:
        return 0

def upload_video(uid,video_title,description,is_public,tags):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO video(video_title,description,creation_time, is_video_public, uploader) \
                VALUES(%s,%s,now(),%s,%s);
                SET @last_vid = LAST_INSERT_ID();"""

            args = [video_title,description,is_public,uid]

            for tag in tags:
                sql += "INSERT IGNORE INTO tag(tag_name) VALUES(%s);"
                sql += "INSERT INTO has_tag(video_vid,tag_tid) VALUES(@last_vid , (SELECT tid FROM tag WHERE tag_name=%s));"
                args.extend([tag]*2)

            cursor.execute(sql,args)
                
        connection.commit()
        return 1
    except Exception as e:
        print(">>",e)
        return 0

def create_playlist(uid,playlist_title,is_playlist_public):
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO playlist(playlist_title,creator,is_playlist_public) VALUES(%s,%s,%s);
                     INSERT INTO has_playlist(playlist_pid,user_uid) VALUES(LAST_INSERT_ID(), %s);"""
            cursor.execute(sql,(playlist_title,uid,is_playlist_public,uid))
        connection.commit()
        return 1
    except Exception as e:
        print(">>",e)
        return 0

def get_is_admin(uid):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM admin WHERE user_uid=%s"
        cursor.execute(sql,uid)
        if cursor.fetchone():
            return 1
        else:
            return 0
