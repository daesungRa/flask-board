import os, sys, json

# json 포맷의 db 관련 환경정보를 호환 객체 타입으로 변환 > string
# os.path.split(os.path.abspath(__file__))[0]
#  > 현재 파일(__file__) 기준으로 절대 경로를 얻어와 그것을 split 한 결과 반환된 list 타입에서 0 번재 인덱스에 저장된 디렉토리 정보를 얻어온다
# os.path.join > 디렉토리 정보와 파일 정보를 재조립
config = json.load(open(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'db_config.json')))