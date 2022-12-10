import pymysql as pms

host = 'localhost'
user='root'
password='root'
charset='utf8mb4'
connection = pms.connect(host=host, user=user, password=password, charset=charset, db='mydb')

def write_comment(uid,vid,comment):
    with connection.cursor() as cursor:
        sql = "INSERT INTO comment(content,write_time,watched_user_uid, watched_video_vid) VALUES(%s,now(),%s,%s)"
        cursor.execute(sql,(comment,uid,vid))
    connection.commit()
    return

def show_comment(vid):
    with connection.cursor() as cursor:
        sql = "SELECT cid, name, content, write_time FROM watched, comment, user WHERE %s=video_vid AND video_vid=watched_video_vid AND uid=watched_user_uid AND user_uid=uid;"
        cursor.execute(sql,(vid))
        comment_list = cursor.fetchall()

        print("result")
        for idx, (_,user_name,comment, write_time) in enumerate(comment_list):
            print(f"\t{idx+1}. user:{user_name}, comment:{comment}, write_time:{write_time}")
        print()
    return

def add_watched_video(uid,vid):
    with connection.cursor() as cursor:
        sql = "INSERT IGNORE INTO watched(user_uid,video_vid) VALUES(%s,%s)"
        cursor.execute(sql,(uid,vid))
    connection.commit()

def get_video_info(vid):
    with connection.cursor() as cursor:
        sql = "SELECT video_title, description, creation_time, uploader FROM video WHERE vid=%s"
        cursor.execute(sql,(vid,))

        video_title, description, creation_time, uploader_uid = cursor.fetchone()

        sql = "SELECT name FROM user WHERE uid=%s"
        cursor.execute(sql,(uploader_uid))
        uploader = cursor.fetchone()[0]

        return video_title, description, creation_time, uploader_uid, uploader

def get_video_tag(vid):
    with connection.cursor() as cursor:
        sql = "SELECT tag_name FROM has_tag,tag WHERE video_vid=%s and tag_tid=tid"
        cursor.execute(sql,(vid,))

        tag_names = [tag[0] for tag in cursor.fetchall()]
        return tag_names

def get_total_video_like(vid):
    with connection.cursor() as cursor:
        sql = "SELECT SUM(is_like) FROM watched WHERE video_vid=%s;"
        cursor.execute(sql,(vid,))

        total_like = int(cursor.fetchone()[0])
        return total_like

def push_like(uid,vid):
    with connection.cursor() as cursor:
        sql = "SELECT is_like FROM watched WHERE user_uid=%s AND video_vid=%s"
        cursor.execute(sql,(uid,vid))
        cur_like = cursor.fetchone()[0]

        if cur_like==0:
            sql = "UPDATE watched SET is_like=1 WHERE user_uid=%s AND video_vid=%s"
        else:
            sql = "UPDATE watched SET is_like=0 WHERE user_uid=%s AND video_vid=%s"
        cursor.execute(sql,(uid,vid))

    connection.commit()

def show_related_videos(vid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT vid,video_title FROM video,related_video WHERE video_vid=%s and vid=rel_video_vid;"
            
            cursor.execute(sql,(vid,))
            recommend_videos = cursor.fetchall()

            if len(recommend_videos)==0:
                return 0
            
            print()
            print("\trecommend videos")
            for idx, (_, video_title) in enumerate(recommend_videos):
                print(f"\t{idx+1}. video title : {video_title}")
            print()
            print("\t\tselect the video number that you want to watch(enter 0 to return)")
            print("\t\tnumber : ",end="")
            video_num = int(input())
            
            if video_num==0:
                return 0

            vid = recommend_videos[video_num-1][0]
            return vid
    except Exception as e:
        print(">>",e)
        return 0

def delete_video(vid):
    with connection.cursor() as cursor:
        sql = "DELETE FROM video WHERE vid=%s"
        cursor.execute(sql,(vid))
    
    connection.commit()

def add_video_into_playlist(uid,vid,pid):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT creator FROM playlist WHERE pid=%s"
            cursor.execute(sql,pid)
            creator = cursor.fetchone()[0]
            assert creator==uid

            sql = "INSERT INTO has_video(playlist_pid,video_vid) VALUES(%s,%s)"
            cursor.execute(sql,(pid,vid))
        connection.commit()
        
        return 1
    except Exception as e:
        print(">>",e)
        return 0


def select_playlist(uid):
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
            print("\tselect the playlist number that you want to add video into(enter 0 to return)")
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