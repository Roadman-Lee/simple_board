from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from board import models
from board.models import Article


class TwoBoardListView(ListView):
    model = models.article.Article
    context_object_name = 'articles' # 객체를 부르는 이름
    # template_name = 'board/index.html'  # default template name

    def get_queryset(self):
        return Article.objects.filter(board_id=2)
        # return Article.objects.filter(board_id=self.request.GET['board_id'])



