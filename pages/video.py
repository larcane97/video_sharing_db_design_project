
from services.video_services import add_video_into_playlist, add_watched_video, delete_video, get_video_info, get_total_video_like, get_video_tag, push_like, select_playlist, show_comment, show_related_videos, write_comment


def video_page(uid,vid):
    while True:
        print("-"*100)
        print("[VIDEO PAGE]")
        add_watched_video(uid,vid)

        video_title, description, creation_time, uploader_uid,uploader = get_video_info(vid)
        video_tags = get_video_tag(vid)
        video_total_like = get_total_video_like(vid)

        print("video title : ",video_title)
        print("description : ",description)
        print("creation time : ", creation_time)
        print("uploader : ",uploader)
        print("video tags : ",", ".join(video_tags))
        print("total like : ",video_total_like)
        print()

        print("0. return to previous page")
        print("1. push like.")
        print("2. write comment.")
        print("3. show comment.")
        print("4. show related videos.")
        print("5. add video into my playlist.")
        print("6. delete video")
        print("Input: ",end="")
        command = int(input())

        if command==0:
            break
        elif command==1:
            push_like(uid,vid)
        elif command==2:
            print("comment : ",end="")
            comment = input()
            write_comment(uid,vid,comment)
        elif command==3:
            show_comment(vid)
        elif command==4:
            related_vid = show_related_videos(vid)
            if related_vid:
                video_page(uid,related_vid)
        elif command==5:
            pid = select_playlist(uid)
            if pid!=0:
                if add_video_into_playlist(uid,vid,pid):
                    print("success adding video into playlist")
                else:
                    print("fail adding video into playlist(ex. no authorization)")
            else:
                print("can't find any playlists.(you should have at least one playlist")
        elif command==6:
            if uploader_uid!=uid:
                print("don't have authorization.")
            else:
                print("you really want to delete the video?(0:NO, 1:YES): ",end="")
                check = int(input())
                if check:
                    delete_video(vid)
                    return 1
        else:
            print("wrong command.")
        