from pages.manage import manage_page
from pages.video import video_page
from pages.playlist import playlist_page
from pages.search import search_page
from services.main_services import account_delete, create_playlist, search_user, search_video, show_commented_videos, show_like_videos, show_playlist, show_upload_video, show_watched_videos, upload_video
from pages.account_info_change import account_info_change_page

def user_main_page(uid):
    while True:
        print("-"*100)
        print("[USER MAIN PAGE]")
        print("0. logout")
        print("1. change user information")
        print("2. delete user account")
        print("3. go to search page")
        print("4. upload a video")
        print("5. create a playlist")
        print("6. show my upload videos")
        print("7. show my playlist")
        print("8. show my like videos")
        print("9. show videos that I commented")
        print("10. show videos that I watched")

        print("Input: ",end="")
        command = int(input())

        if command==0:
            break
        elif command==1:
            account_info_change_page(uid)
        elif command==2:
            print("enter password to delete account.")
            print("password : ",end="")
            password = input()
            if account_delete(uid,password):
                print("success deleting account")
                break
            else:
                print("fail deleting account")
        elif command==3:
            search_page(uid)
        elif command==4:
            print("video title: ",end="")
            video_title = input()

            print("description: ",end="")
            description =input()

            print("upload video in public(0:NO, 1:YES): ",end="")
            is_public = int(input())

            print("video tags : ",end="")
            tags = input().split()

            if upload_video(uid,video_title,description,is_public,tags):
                print("success uploading video.")
            else:
                print("fail uploading video.")
        elif command==5:
            print("playlist title: ",end="")
            playlist_title = input()

            print("create playlist in public(0:NO, 1:YES): ",end="")
            is_playlist_public = int(input())

            if create_playlist(uid=uid,playlist_title=playlist_title,is_playlist_public=is_playlist_public):
                print("success creating playlist.")
            else:
                print("fail creating playlist")
        elif command==6:
            vid = show_upload_video(uid,uid)
            if vid:
                video_page(uid,vid)
        elif command==7:
            pid = show_playlist(uid)
            if pid:
                playlist_page(uid,pid)
        elif command==8:
            vid = show_like_videos(uid)
            if vid:
                video_page(uid,vid)
        elif command==9:
            vid = show_commented_videos(uid)
            if vid:
                video_page(uid,vid)
        elif command==10:
            vid = show_watched_videos(uid)
            if vid:
                video_page(uid,vid)
        else:
            print("wrong command.")

def admin_main_page(uid):
    while True:
        print("-"*100)
        print("[ADMIN MAIN PAGE]")
        print("0. logout")
        print("1. change admin information")
        print("2. delete admin account")
        print("3. go to search page")
        print("4. go to manage page")

        print("Input: ",end="")
        command = int(input())

        if command==0:
            break
        elif command==1:
            account_info_change_page(uid)
        elif command==2:
            print("enter password to delete account.")
            print("password : ",end="")
            password = input()
            if account_delete(uid,password):
                print("success deleting account")
                break
            else:
                print("fail deleting account")
        elif command==3:
            search_page(uid)
        elif command==4:
            manage_page(uid)
        else:
            print("wrong command.")