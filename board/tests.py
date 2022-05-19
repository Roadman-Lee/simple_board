from django.test import TestCase

from board.models.article import Article


class AnyTest(TestCase):
    def test_setUp(self):
        board = Article.objects.create(board_id=1, title="네번째 메세지 내용", article="네번째 메세지 내용", password=1234,
                                     nickname='unknown')
        msg = Article.objects.get(board_id=1).title
        self.assertEqual("네번째 메세지 내용", msg)
