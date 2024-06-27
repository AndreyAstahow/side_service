from django.urls import path
from .views import (
    IndexView, PersonalCab, PostView, PostCreate, PostDetail, PostDelete
    )

urlpatterns = [
    path('', IndexView.as_view()),
    path('lc/', PersonalCab.as_view()),
    path('mon/', PostView.as_view(), name='post_list'),
    path('mon/create/', PostCreate.as_view()),
    path('mon/detail/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('mon/detail/<int:pk>/delete/', PostDelete.as_view())
] 