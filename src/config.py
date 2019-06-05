import os, json

# base dir test
# print(os.path.split(os.path.abspath(__file__))) # split 결과, list 형태로 반환함
# print(os.path.split(os.path.abspath(__file__))[0]) # 첫 번째 인덱스는 dir 까지
# print(os.path.abspath(os.path.dirname(__file__))) # 더욱 간단하게

# json 포맷의 db 관련 환경정보를 호환 객체 타입으로 변환 > string
# os.path.split(os.path.abspath(__file__))[0]
#  > 현재 파일(__file__) 기준으로 절대 경로를 얻어와 그것을 split 한 결과 반환된 list 타입에서 0 번재 인덱스에 저장된 디렉토리 정보를 얻어온다
# os.path.join > 디렉토리 정보와 파일 정보를 재조립
basedir = os.path.abspath(os.path.dirname(__file__))
# print('basedir\t\t\t\t\t\t\t: ' + basedir)
# print('basedir + json db config file\t: ' + os.path.join(basedir, 'db_config.json'))

config = json.load(open(os.path.join(basedir, 'db_config.json')))

# random unit test
# import random
# from random import shuffle, choice
#
# print('random : ' + str(random.randrange(1, 11)))
# abc = [1,2,3,4,5,6,7,8,9,10]
# shuffle(abc)
# print('shuffle : ' + str(abc))
# print('choice : ' + str(choice(abc)))

