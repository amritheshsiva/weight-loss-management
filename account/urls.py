from django.urls import path
from account import views
urlpatterns= [
    path('',views.login_page,name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout')
]