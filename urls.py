from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('',views.sign,name='sign'),
    path('predict/',views.predict_next_words,name="predict"),
    path('words', views.words,name="words"),
    path('login', views.login_page, name='login'),
    path('logout',views.Logoutpage,name="logout")

]