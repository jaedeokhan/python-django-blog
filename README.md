# Python Django 간단한 Blog 프로젝트

## 개발 환경 => [requirements.txt](https://github.com/jaedeokhan/Blog-Django/blob/main/requirements.txt)

* Python Version 3.8
* Django Version 3.1.2
   * pip install Django
* Pillow Version 8.0.1 
   * Pillow는 Django models.py에서 imageField를 사용하기 위해서 설치해야한다.
   * pip install pillow Or python -m pip install pillow

## 기능 구성
#### 블로그의 생성, 수정, 삭제, 리스트, 상세정보 모두 django에서 제공하는 gerenic View를 사용했습니다. 
#### 조회수는 models.py에 29행에 @property를 이용해서 구현했습니다. 
#### 추천수는 ajax를 통해서 페이지 전부를 로드시키지 않고, 일부 기능만 통신을 해서 구현했습니다.
#### 로그인, 로그아웃은 admin.py에서 제공하는 accounts/login, accounts/logout을 사용했습니다.

1. 블로그 게시물 등록, 수정, 삭제, 리스트, 상세정보기능(CreateView, UpdateView, DeleteView, ListView, DetailView)
2. 블로그 조회수 기능(view_count)
3. 블로그 추천수 기능(likes_user)
4. 로그인, 로그아웃 기능(accounts/login, accounts/logout)

