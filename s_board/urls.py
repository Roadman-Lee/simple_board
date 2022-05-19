from django.urls import path

from . import views

urlpatterns = [
    path('', views.TwoBoardListView.as_view(), name='s_board')
]