from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('frontpage',views.frontpage,name='frontpage'),
    path('',views.start,name='start'),
    path('signup/',views.signup,name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name='chatApp/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),

        path('sell_book/', views.sell_book, name='sell_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('book/<str:book_name>/<str:author_name>/', views.book_detail, name='book_detail'),
]