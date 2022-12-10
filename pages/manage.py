from services.video_services import show_related_videos
from services.manage_services import manage_recommend_videos, manage_video_comment
from pages.video import video_page
from services.main_services import search_user, search_video, show_watched_videos


def manage_page(uid):
    while True:
        print("-"*100)
        print("[MANAGE MAIN PAGE]")
        print("0. return to previous page")
        print("1. check a user's watched videos")
        print("2. check a video's comment")
        print("3. check a video's recommend videos")
        print("4. set recommend videos")

        print("Input: ",end="")
        command = int(input())

        if command==0:
            break
        elif command==1:
            print("enter user name that you want to search.")
            print("user name : ",end="")
            user_name = input()
            search_uid = search_user(user_name)
            vid = show_watched_videos(search_uid)
            if vid:
                video_page(uid,vid)
        elif command==2:
            print("enter video title that you want to search.")
            print("video title: ",end="")
            video_title = input()
            vid = search_video(video_title)
            if vid:
                manage_video_comment(vid)
        elif command==3:
            print("enter video title that you want to search.")
            print("video title: ",end="")
            video_title = input()
            vid = search_video(video_title)
            if vid:
                show_related_videos(vid)
        elif command==4:
            print("enter video title that you want to search.")
            print("video title: ",end="")
            video_title = input()
            vid = search_video(video_title)
            manage_recommend_videos(vid)

