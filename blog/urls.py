from django.urls import path
from .views import *

urlpatterns = [
    # post views
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:post>/',
        post_detail,
        name='post_detail'),
]
