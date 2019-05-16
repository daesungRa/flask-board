
### 참조 프로젝트 : [mrxmamun](https://github.com/mrxmamun) 의 [flask-mvc-pymongo](https://github.com/mrxmamun/flask-mvc-pymongo)

## 프로젝트 설명

- 목적
    * todo list 를 작성하여 mongodb 서버에 저장하기
    * 작성한 todo 요소에 대한 update 및 delete 가능
- 특징
    * html form 형태로 요청
        - 각 요청 기반은 create 시 자동 생성된 "_id" 필드값이다.
        - get : get todo list
        - post : execute insert_one action
        - put : execute update_one action
        - delete : execute delete_one action
    * 특별한 사용자지정 모듈 사용
        ```text
        - app
            - todo
              ㄴ validation
              ㄴ database
        ```
        - **app** 은 flask 웹앱이다
        - **todo** 는 웹앱이 사용하는 메인 모듈이다.
        - **validation** 은 입력된 json 데이터의 유효성을 체크하여 todo 에 전달하는 모듈이다. (요구되는 필드값이 있는지)
        - **database** 는 유효한 데이터를 mongodb 서버에 저장하고 그 결과를 리턴하는 모듈이다.
- 기타
    * 로컬에서 mongodb 서버를 구동하고, flask 는 pymongo 모듈을 통해 접근 가능하다.
    * 아직 퍼블리싱된 프론트 및 정적 파일은 존재하지 않는다.
    * 임의의 데이터를 insert 하고 브라우저로 테스팅 해보면 잘 돌아간다! (190515, wed)



