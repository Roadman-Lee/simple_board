import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from board.models import Article
from y_board import kornum
# test
from django.views.generic import ListView


class TestViews(ListView):
    context_object_name = 'testList'

    def get_queryset(self):
        return Article.objects.filter(board_id=3)





def board(request):
    return HttpResponse("hello world")


def insert(request):
    if request.method == 'GET':  # method가 post일때
        y, k, l = 0, 0, 0
        limit_num = 500

        while y <= limit_num and k <= limit_num and l <= limit_num:
            board_id = random.randrange(1, 4)
            if board_id == 1 and y <= limit_num:
                y += 1
                test_insert_article(board_id=board_id, num=y)
            if board_id == 2 and k <= limit_num:
                k += 1
                test_insert_article(board_id=board_id, num=k)
            if board_id == 3 and l <= limit_num:
                l += 1
                test_insert_article(board_id=board_id, num=l)

        return HttpResponse('우왕 성공했어요 헤헷', status=200)

    else:
        return HttpResponse(status=404)


# 단순 서비스 함수
def test_insert_article(board_id, num=1):
    # 수사 (하나 둘 셋)
    numeral = kornum.convert(num, 수사='양수사-관형사', 한자어=False)
    return Article.objects.create(board_id=board_id, title=f"{numeral}번째 제목",
                                  article=f"{numeral}번째 글귀 \n {random_name_or_msg(1)}", password=1234,
                                  nickname=random_name_or_msg())


# 랜덤 게시글 내용
def random_name_or_msg(name_msg=0):
    file_name = 'name.txt'
    if name_msg:
        file_name = 'text.txt'

    with open(file_name, 'r', encoding="UTF-8") as f:
        random_txt = random.choice(list(f.readlines())).splitlines()[0]
    return random_txt

# set FOREIGN_KEY_CHECKS = 1;
# truncate table board_article;
