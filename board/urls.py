from django.urls import path

from board import views

urlpatterns = [
    path("", views.board, name="board"),
    path('insert/', views.insert, name="board_insert")
]
