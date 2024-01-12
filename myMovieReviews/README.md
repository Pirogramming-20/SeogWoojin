구현한 기능: 1,2,3,4,5,6,7,8,9,10,11

구현하지 못한 기능: X

🔥 챌린지 참여합니다! 🔥
프론트는 과제 화면을 참고했습니다!

장르 선택 기능 & 별점, 개봉년도, 제목 순으로 정렬 기능 & 러닝타임 시간 단위로의 출력 기능 구현 완료했습니다!😎


## 메인 화면 (/reviews) 
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
'''
- 기본 (평점 순 정렬)
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/0f08ccf3-1a08-474a-af47-c79deae82ff0">
- 제목 순
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/713d6de8-1256-44b5-ba3c-5b33719da766">
- 개봉년도 순 
<img width="800" alt="image" src="https://github.com/Pirogramming-20/SeogWoojin/assets/121532823/1d85205e-a69b-46a2-b1d4-6104f5672ee8">


