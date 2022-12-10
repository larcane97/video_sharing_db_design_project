from pages.playlist import playlist_page
from pages.video import video_page
from services.main_services import get_is_admin, search_playlist, search_user, search_video, show_upload_video

def search_page(uid):
    is_admin = get_is_admin(uid)
    while True:
        print("-"*100)
        print("[SEARCH PAGE]")
        print("0. return to previous page")
        print("1. search a user")
        print("2. search a video")
        print("3. search a playlist")

        print("Input:",end=" ")
        command = int(input())
        
        if command==0:
            break
        elif command==1:
            print("enter user name that you want to search.")
            print("user name : ",end="")
            user_name = input()
            search_uid = search_user(user_name) # (uid,user_name)

            if search_uid:
                vid = show_upload_video(uid,search_uid)
                if vid:
                    video_page(uid,vid)
        elif command==2:
            print("enter video title that you want to search.")
            print("video title: ",end="")
            video_title = input()
            vid = search_video(video_title,is_admin) # (uid,user_name)
            if vid:
                video_page(uid,vid)
        elif command==3:
            print("enter playlist title that you want to search.")
            print("playlist title: ",end="")
            playlist_title = input()
            pid = search_playlist(playlist_title,is_admin) # (uid,user_name)
            if pid:
                playlist_page(uid,pid)
        else:
            print("wrong command")

