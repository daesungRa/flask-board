import math
from src.factory.database import Database

class Pagination(object):
    def __init__(self):
        self.db = Database()

        self.pagesize = 20 # 페이지 사이즈
        self.blocksize = 5 # 블럭 사이즈
        self.nowpage = 1 # 현재 페이지 (기본 1 페이지)

        self.totalcount = 0
        self.maxpage = 0
        self.maxblock = 0
        self.nowblock = 0

        self.endpage = 0
        self.startpage = 0

    def tot_pagination(self, nowpage, collection_name):
        self.nowpage = nowpage # nowpage 세팅
        self.totalcount = self.db.count(collection_name) # 전체 도큐먼트 개수

        self.maxpage = math.ceil(self.totalcount / self.pagesize) # 전체(마지막) 페이지 (잉여 도큐먼트 포함해서 올림)
        self.maxblock = math.ceil(self.maxpage / self.blocksize) # 전체(마지막) 블럭 (잉여 페이지 포함해서 올림)
        self.nowblock = math.ceil(self.nowpage / self.blocksize) # 현재 블럭

        # 각 페이지와 블럭에 대한 세부처리
        self.endpage = self.nowblock * self.blocksize
        self.startpage = self.endpage - self.blocksize + 1
        if self.endpage > self.maxpage: # 마지막 블럭일 경우
            self.endpage = self.maxpage

        print('nowpage: ' + str(self.nowpage))
        print('totalcount: ' + str(self.totalcount))
        print('maxpage: ' + str(self.maxpage))
        print('maxblock: ' + str(self.maxblock))
        print('nowblock: ' + str(self.nowblock))
        print('endpage: ' + str(self.endpage))
        print('startpage: ' + str(self.startpage))



