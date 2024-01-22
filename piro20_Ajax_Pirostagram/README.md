~~저는 꺾였습니다.. 건들다만 css는 너그럽게 용서해주시길..~~

### 기능 설명


- 좋아요 기능 구현
  1. 체크 / 비체크 이미지 구분
  2. 로그인 하지 않으면 하트를 눌러도 색만 바뀔 ( @login_required 사용, 서버 데이터와 무관)
  3. 로그인 유저가 좋아요를 눌렀던 글은 새로고침해도 좋아요 눌러진 상태로 구현 (그 상태로 버튼을 누를 시 좋아요 취소)


  <img width="527" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/d0ad24e1-821e-41d2-8fe3-edde570f163d">

  유저 모델 N:M 관계 Manytomany 이용, 좋아요 수는 likes라는 필드로 따로 관리
  
  css와 label for를 통해서 체크 / 비체크를 색으로 구분했으며
  
  <img width="491" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/e2b15680-e000-4463-b949-f28379e4c75d">
  
  js의 change_like 함수에서 httprequest를 통해 box 체크 여부에 따라 생성된 json 데이터를 통한 비동기 처리를 통해서 like_users 생성(삭제) 성공 후, 좋아요 수를 변경했습니다.

- 댓글 작성
  1. 댓글 작성 유저와 내용 확인 가능
  2. 본인이 작성한 댓글만 삭제 버튼 뜸
  3. 로그인 하지 않으면 작성 불가
  4. Input이 비어있으면 작성 불가
  
  <img width="593" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/0e47b8a6-ddd1-4ea3-90f4-ff41ed9281f8">

  댓글 모델에 Post와 User 모델을 각각 매핑해 다대다 관계에 내용만 추가한 형태입니다.

  <img width="569" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/4a69b725-6331-4bba-8023-4e8c99fcf171">

  onclick을 통해 commentUp함수를 선언해 선언한 Post의 input 내용을 가져온 후 ( 비어있다면 에러처리 )
  서버에 postid 와 댓글 내용을 json 데이터로 보내주고, Comment 인스턴스 생성, Comment의 id를 view에서 반환하면
  타 댓글들과 동일한 형태의 element 생성 후 추가, input 내용은 다시 처음 형태로 비워놓습니다.
  

- 삭제
  1. 비동기로 추가한 댓글도 곧바로 삭제 가능함

  <img width="588" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/5f08afc7-890c-4dc2-862d-fe67cd68281a">

  동일하게 delete_comment로 비동기 작업 진행, server의 경우 comment.delete() 를 통해서 템플릿의 경우 element.remove(); 를 통해서 진행했습니다.
  

- 유저, 게시글 생성 기능
  1. 간단한 CR 을 통해서 이미지 업로드 가능하도록 설정했습니다. 




