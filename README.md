
### 참조 프로젝트 : [mrxmamun](https://github.com/mrxmamun) 의 [flask-mvc-pymongo](https://github.com/mrxmamun/flask-mvc-pymongo)

## 프로젝트 설명

- 목적
    * 기존의 validation 모듈을 개조해서 활용한 입력 데이터 체크 게시판
- 특징
    * html form 형태로 요청
        - 각 요청 기반은 create 시 자동 생성된 "_id" 필드값이다.
        - get : get board list
        - post : execute insert_one action
        - put : execute update_one action
        - delete : execute delete_one action
    * 특별한 사용자지정 모듈 사용
        ```text
        - app
            - service
              ㄴ validation
              ㄴ database
        ```
        - **app** 은 flask 웹앱이다
        - **service** 는 웹앱이 사용하는 메인 모듈이다.
        - **validation** 은 입력된 json 데이터의 유효성을 체크하여 service 에 전달하는 모듈이다. (요구되는 필드값이 있는지)
        - **database** 는 유효한 데이터를 mongodb 서버에 crud 하고 그 결과를 리턴하는 모듈이다.
- 기타
    * 로컬에서 mongodb 서버를 구동하고, flask 는 pymongo 모듈을 통해 접근 가능하다.
    * 아직 퍼블리싱된 프론트 및 정적 파일은 존재하지 않는다. (이제 존재한다, 190522, wed)
    * 임의의 데이터를 insert 하고 브라우저로 테스팅 해보면 잘 돌아간다! (190515, wed)
    * jinja2 매크로 만들어 적용하기 (중복 코드 제거)
- 보수할 사항 **(190522, wed 기준)**
    * url 에 get 방식으로 나타나는 id 값 제거하기
    * app.py 에서 공통 코드 합치기
        - board 와 todo 라우팅에 있어서 uri 만 다르고 함수 로직은 동일하기 때문에 코드 간략화의 가능성이 있다
        - service 모듈의 인스턴스명도 board 에서 service 로 더 추상화한다.
    * 회원관리를 위한 세션 및 쿠키 공부 후 적용하기
    * 댓글 기능 구현하기
    * 회원관리, 관리자 기능 및 페이지 추가하기
    * 메인 화면에 타임라인 추가, 게시글 및 todo 리스트 요약해서 보여주기
    * 파일업로드 관련 로직 구상해서 적용하기


