구현한 기능 : 1~15

챌린지 도전합니다!
🥊 챌린지 한 페이지 당 4개의 게시물만 보이도록 페이지네이션 처리 구현
🥊 챌린지 name으로 개발툴을 찾는 검색 구현 (ajax 또는 쿼리스트링 활용) 구현


간단한 설명

- 기존 crud는 이전 과제들을 참조했습니다. 

- html, css의 경우 토요일 수업틀과 과제설명 pdf를 참고했습니다.

- 찜하기, 관심도는 js의 ajax문을 이용해서 click event 발생시 실행되도록 했습니다.

- 찜하기의 Ideastar 모델은 Idea 모델과 1대1 매핑이 되어있으며, Idea 모델 생성시 star 필드에 default값으로 False가 설정된 Ideastar 데이터가 동시에 생성됩니다.

- mouseover 함수를 이용해서 각각의 아이디어의 썸네일에 마우스가 올라가면 별이 항상 보이도록 설정했습니다.

- 정렬의 경우 query param을 이용했고, select의 경우 js를 이용했습니다

- 페이징은 from django.core.paginator import Paginator 라는 내부 기술을 활용해 구현했습니다. 정렬과의 쿼리 충돌을 막기위해 &sort={{ order_by_field }}를 href에 추가했습니다.

