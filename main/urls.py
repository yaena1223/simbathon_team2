from django.urls import path
from .views import *

app_name="main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('academic/', academic, name="academic"),
    path('volunteer/', volunteer, name="volunteer"),
    path('research/', research, name="research"),
    path('art/', art, name="art"),
    path('fresh/', fresh, name="fresh"),
    path('performance/', performance, name="performance"),
    path('atheletic/', atheletic, name="atheletic"),
    path('social/',social,name='social'),
    path('contact/',contact,name='contact'),
    path('likelion/',likelion,name='likelion'),
    path('<str:id>',detail,name='detail'),
    path('new/',new,name='new'),
    path('create/',create,name='create'),
    path('edit/<str:id>',edit,name='edit'),
    path('update/<str:id>',update,name='update'),
    path('delete/<str:id>',delete,name='delete'),
]