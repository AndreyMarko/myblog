from django.urls import path
from . import views
from .views import robots_txt

urlpatterns = [path("", views.PostView.as_view()),
               path('dostavka/', views.Dostavka.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComents.as_view(), name='add_comments'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
               path('<int:pk>/del_likes', views.DelLike.as_view(), name='dell_likes'),
               path("robots.txt", robots_txt)]



