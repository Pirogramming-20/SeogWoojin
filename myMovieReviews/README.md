구현한 기능: 1,2,3,4,5,6,7,8,9,10,11

구현하지 못한 기능: X

🔥 챌린지 참여합니다! 🔥
프론트는 과제 화면을 참고했습니다!

- 장르 선택 기능 (charField 의 choices 인자 사용)
- 별점, 개봉년도, 제목 순으로 정렬 기능 (html:select, python:order_by, js:정렬방식 셀렉트 박스 유지)
- 러닝타임 시간 단위로의 출력 기능 (get한 객체의 running_time 변수를 확인하여 60 전후로 나눴고, html에선 django html 문법 if를 사용) 
  
구현 완료했습니다!😎




> 세부 기능 설명

#### 메인 화면 (/reviews) 
파이썬에서 리뷰 리스트를 받아와 html에서 정렬 후 출력
정렬 구현의 경우, html의 select, option 태그와 js를 이용해, get에서 받아온 파라미터를 바탕으로 정렬합니다
``` python
    sort = request.GET.get('sort','')
    if sort == 'title':
        content_list = Review.objects.all().order_by('title')
    elif sort ==  'years':
        content_list = Review.objects.all().order_by('-release_date')
    else:
        content_list = Review.objects.all().order_by('-stars')    
```
- 평점 순 (기본 정렬)
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/0f08ccf3-1a08-474a-af47-c79deae82ff0">

- 제목 순
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/713d6de8-1256-44b5-ba3c-5b33719da766">

- 개봉년도 순 
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/1d85205e-a69b-46a2-b1d4-6104f5672ee8">

#### 리뷰 작성 화면 (/reviews/create)
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/b5ad3700-83e5-4667-897f-822e570f4282">

forms.py를 이용해 form.as_p로 form 구현을 간단하게 진행했습니다. 
사진의 경우, 등록 기능을 따로 넣진 않았고 만약 넣고 싶다면 reviews/static/image에 jpg파일의 이름을 제목과 동일하게 저장하면 불러올 수 있습니다. 
( review.image=f"static/images/{review.title}.jpg" 구문 참고 )

#### 리뷰 세부 페이지 (/reviews/detail/{{pk}})
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/78fa5a16-552d-41de-bdd9-bdb83b601b65">

별다를 건 없고, pk를 이용해 get해온 객체를 html 형식에 담았다. 60분의 여부에 따라 시간이 나뉜다는 점

#### 리뷰 수정 페이지 (/reviews/edit/{{pk}})
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/d9c8c838-05d5-4465-8cc0-2b66cf9f6360">

form과 기존 데이터 베이스 객체를 연결시키는 코드 -> form = ReviewForm(request.POST, instance=review)

#### 리뷰 삭제 
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/b3d44e90-e932-4b4b-baf9-3c2a120e0078">

데이터베이스에서 꺼내온 객체에 delete 함수 사용



..앞으로
restful한 api 작성, 아무래도 M to N 데이터를 다루는 게 조금 난이도 있을 것 같다.
