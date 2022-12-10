
from services.playlist_services import add_to_my_playlist, delete_playlist, get_playlist_info


def playlist_page(uid,pid):
    while True:
        print("-"*100)
        print("[PLAYLIST PAGE]")

        playlist_title, creator, creator_uid, playlist_video_info = get_playlist_info(uid,pid)
        print(f"playlist title : {playlist_title}, creator : {creator}")
        print("playlist items : ")
        for idx,(_,_, video_title, uploader, creation_time) in enumerate(playlist_video_info):
            print(f"\t{idx+1}. video title:{video_title}, uploader:{uploader}, creation_time:{creation_time}")
        print()

        print("0. return to previous page")
        print("1. add to my playlist.")
        print("2. delete the playlist.")
        print("Input: ",end="")

        command = int(input())

        if command==0:
            break
        elif command==1:
            if add_to_my_playlist(uid,pid):
                print("success adding this playlist to my playlists")
            else:
                print("fail adding this playlist to my playlists.(already exists or wrong infomation.)")
        elif command==2:
            if creator_uid!=uid:
                print("don't have authorization.")
            else:
                print("you really want to delete this playlist?(0:NO, 1:YES): ",end="")
                check = int(input())
                if check:
                    delete_playlist(pid)
                    return 1
        else:
            print("wrong command.")
        