## 영상 공유 사이트 DB 설계 프로젝트
해당 저장소는 "사용자간 영상을 업로드하고 공유할 수 있는 사이트의 DB 설계 및 CLI기반 데모 제작"을 구현한 코드입니다.

<br>
<br>

### DB dump
아래 명령어를 통해 DB dump를 mysql DBMS에 저장

`mysql -u [username] -p {password} [dbname] < db_dump.sql`


해당 프로그램은 mysql이 localhost:3306에 열려있다고 가정하고 코드를 작성하였습니다.

__ERD__
![ERD](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/72dc045b-da08-4c1a-b462-c0d4e76ca7ad/youtube_db_ERD.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221210T122806Z&X-Amz-Expires=86400&X-Amz-Signature=632365c9c0730071ae9d1912dbdcf12692408dd88e49cbf610a5711d33aaa732&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22youtube_db_ERD.png%22&x-id=GetObject)

<br>
<br>

### 실행
아래 명령어를 통해 데모 CLI 실행

`python3 program.py`


<br>
<br>

### 요구사항

__사용자__
- 사용자는 이름, id, password, 이메일을 필수로 가지고 있어야 한다.
- id와 이메일은 다른 사용자와 동일한 값을 사용할 수 없다.
- uid는 각 사용자를 구분하기 위한 id로, 사용자가 생성될 때마다 자동적으로 부여된다.
- 사용자는 영상을 업로드 하고 본인의 업로드 영상 목록을 관리할 수 있다.
- 사용자는 업로드된 다른 사람의 영상을 볼 수 있다.
- 사용자는 자신만의 영상 재생 리스트를 만들 수 있다.
- 사용자는 자신이 업로드한 영상의 공개 여부를 설정할 수 있다.
- 사용자는 자신의 영상 재생 리스트의 공개 여부를 설정할 수 있다.
- 사용자는 현재 자신이 보고 있는 영상에 “좋아요”를 표시할 수 있다.
- 사용자는 현재 자신이 보고 있는 영상에 “댓글”을 작성할 수 있다.
- 사용자는 현재 자신이 보고 있는 영상과 유사한 영상 목록을 볼 수 있다.
- 사용자는 특정 사용자의 이름을 검색해 해당 사용자의 영상 목록을 볼 수 있다.
- 사용자는 특정 영상 제목을 검색해 찾을 수 있다.
- 사용자는 특정 플레이리스트 제목을 검색해 찾을 수 있다.
- 사용자는 특정 태그를 검색해 관련 태그 영상을 찾을 수 있다.
- 사용자는 자신이 “좋아요”한 영상 목록을 볼 수 있다.
- 사용자는 자신이 “댓글”을 작성한 영상 목록을 볼 수 있다.
- 사용자는 자신이 시청한 영상의 목록을 볼 수 있다.

<br>

__관리자__
- 관리자는 이름, id, password, 이메일을 필수로 가지고 있어야 한다.
- id와 이메일은 다른 관리자와 동일한 값을 사용할 수 없다.
- aid는 각 관리자를 구분하기 위한 id로, 관리자가 생성될 때마다 자동적으로 부여된다.
- 관리자는 각 사용자의 영상 업로드 내역과 시청 내역을 관리한다.
- 관리자는 특정 영상의 관련 영상을 관리한다.
- 관리자는 특정 영상의 “댓글” 내역을 관리한다.

<br>

__영상__
- 영상을 생성할 때 반드시 제목을 입력해야 한다.
- 생성자에는 영상을 업로드한 사용자의 uid가 자동으로 부여된다.
- vid는 각 영상을 구분하기 위한 id로, 영상이 생성될 때마다 자동적으로 부여된다.
- 설명란에서 생성자가 작성한 영상의 설명을 확인할 수 있다.
- 영상을 나타내는 “태그”를 가질 수 있다.
- 영상에서 받은 전체 “좋아요” 개수와 전체 “댓글” 개수를 확인할 수 있다.
- 영상에서 어떤 유저가 어떤 “댓글”을 작성했는지 확인할 수 있다.
- 영상에서 어떤 유저가 어떤 “댓글”을 언제 작성했는지 확인할 수 있다.
- 공개여부는 영상의 생성자가 해당 영상을 공개 한다면 1로, 비공개 한다면 0으로 설정된다.

<br>

__플레이리스트__
- 플레이리스트를 생성할 때 반드시 제목을 입력해야 한다.
- 생성자는 플레이리스트를 생성한 사용자의 uid가 자동으로 부여된다.
- pid는 각 플레이리스트를 구분하기 위한 id로, 플레이리스트가 생성될 때마다 자동적으로 부여된다.
- 영상개수는 플레이리스트에 포함된 영상의 개수에 따라 자동으로 부여된다.
- 공개여부는 플레이리스트의 생성자가 해당 플레이리스트를 공개 한다면 1로, 비공개 한다면 0으로 설정된다.

<br>

__태그__
- 태그는 고유한 tid와 이름을 가지고 있어야 한다.
- 사용자가 기존에 없던 태그를 영상에 부여하면 새로운 태그가 생성되어야 한다.
- tid는 각 태그를 구분하기 위한 id로, 태그가 생성될 때마다 자동적으로 부여된다.

<br>
<br>