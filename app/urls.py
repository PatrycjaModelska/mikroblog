"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from microblog.views import (Microblog_about,
                             PostList,
                             PostAdd,
                             PostDetail,
                             post_edit,
                             post_delete,
                             CommentAdd,
                             PostManager,
                             MyMicroblog,
                             Top5,
                             TitleContextSerching,
                             CategorySerching, )
from users.views import registration, user_login, user_logout


urlpatterns = [
    path('admin/', admin.site.urls),

    # users app

    path('logowanie/', user_login, name='Login'),
    path('wylogowanie/', user_logout, name='Logout'),
    path('rejestracja/', registration, name='Registration'),



    # mikroblog app
    path('about/', Microblog_about, name='Microblog_about'),

    path('', PostList.as_view(), name='Home_page'),

    path('dodajpost/', PostAdd.as_view(), name='Post_add'),
    path('post/<int:pk>/', PostDetail.as_view(), name='Post_detail'),
    path('post/<int:pk>/edytuj/', post_edit, name='Post_edit'),
    path('post/<int:pk>/usun', post_delete, name='Post_delete'),

    path('post/<int:pk>/dodajkomentarz', CommentAdd.as_view(), name='Comment_add'),

    path('zarzadzajpostami/', PostManager.as_view(), name='Post_manager'),
    path('mikroblog/<str:id_author>', MyMicroblog.as_view(), name='My_microblog'),

    path('top_posts/', Top5.as_view(), name='Top_posts'),

    path('ratings/', include('star_ratings.urls', namespace='ratings')),

    path('wyszukiwanie/', TitleContextSerching.as_view(), name='Wyszukiwanie'),
    path('wyszukiwanie/<str:category>/', CategorySerching.as_view(), name='Category_serching'),

]
