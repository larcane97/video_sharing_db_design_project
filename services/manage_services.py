from services.main_services import search_video
import pymysql as pms

host = 'localhost'
user='root'
password='root'
charset='utf8mb4'
connection = pms.connect(host=host, user=user, password=password, charset=charset, db='mydb')

def manage_video_comment(vid):
    try:
        with connection.cursor() as cursor:
            while True:
                print()
                sql = "SELECT cid, name, content, write_time FROM watched, comment, user \
                       WHERE %s=video_vid AND user_uid=watched_user_uid AND video_vid=watched_video_vid AND user_uid=uid;"
                cursor.execute(sql,(vid))
                comment_list = cursor.fetchall()

                sql = "DELETE FROM comment WHERE cid=%s"
                print("result")
                for idx, (_,user_name,comment, write_time) in enumerate(comment_list):
                    print(f"\t{idx+1}. user:{user_name}, comment:{comment}, write_time:{write_time}")
                print()
                print("\tselect the playlist number that you want to delete(enter 0 to finish)")
                print("\tnumber : ",end="")
                comment_num = int(input())

                if comment_num==0:
                    break
                cid = comment_list[comment_num-1][0]
                cursor.execute(sql,(cid,))
        connection.commit()
        return 1
    except Exception as e:
        print(">>",e)
        return 0

def manage_recommend_videos(vid):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO related_video VALUES(%s,%s)"
            while True:
                print("search videos to set recommend video(enter 0 to finish)")
                print("video title: ",end="")
                recommend_video_title = input()
                if recommend_video_title=='0':
                    break
                recommend_vid = search_video(recommend_video_title)
                cursor.execute(sql,(vid,recommend_vid))
        connection.commit()
        return 1
    except Exception as e:
        print(">>",e)
        return 0