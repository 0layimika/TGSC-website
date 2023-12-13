from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('<int:blog_id>/add_comment/', views.add_comment, name='add_comment'),
    path('<int:blog_id>/detail',views.detail, name='detail'),
    path('all',views.all,name='all'),
    path('contact',views.contact,name='contact'),
    path('about', views.about, name="about")
]