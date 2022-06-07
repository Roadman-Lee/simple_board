import random

from django.test import TestCase

from board.models import Article
from y_board import kornum


# 여러개의 게시글 생성하기위한 클래스
class Board:
    def __init__(self, board_id: int):
        self.board_id = board_id
        self.created_cnt = 1

    # 게시글 랜덤하게 생성해주는 함수
    def create_article(self) -> int:
        numeral = kornum.convert(self.created_cnt, 수사='양수사-관형사', 한자어=False)

        try:
            Article.objects.create(
                board_id=self.board_id, title=f"{numeral}번째 제목",
                article=f"{numeral}번째 글귀 \n {self.random_name_or_msg(1)}", password=1234,
                nickname=self.random_name_or_msg()
            )
            self.created_cnt += 1
            code = 202
        except:
            self.created_cnt += 1
            code = 500
        finally:
            return code

    # 랜덤한 글쓴이 또는 메세지 생성기
    def random_name_or_msg(self, name_msg=0) -> str:
        file_name = 'name.txt'
        if name_msg:
            file_name = 'text.txt'

        with open(file_name, 'r', encoding="UTF-8") as f:
            random_txt = random.choice(list(f.readlines())).splitlines()[0]
        return random_txt


class AnyTest(TestCase):
    LIMIT_NUM = 10

    # 게시글 단순 한가지 생성해보는 함수
    def test_setUp(self):
        board = Article.objects.create(board_id=1, title="네번째 메세지 내용", article="네번째 메세지 내용", password=1234,
                                       nickname='unknown')
        msg = Article.objects.get(board_id=1).title
        self.assertEqual("네1번째 메세지 내용", msg)

    # 게시글 LIMIT_NUM 수만큼 생성해주는 서비스
    def test_inserts(self):
        boards = [Board(1), Board(2), Board(3)]

        while all(bd.created_cnt <= self.LIMIT_NUM for bd in boards):
            random_board_index = random.randrange(len(boards))
            boards[random_board_index].create_article()

        self.assertEqual(Article.objects.first().title, '첫번째 제목')
        self.assertEqual(Article.objects.last().title, '열번째 제목')
