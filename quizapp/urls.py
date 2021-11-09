
from django.urls import path, include
from . import views

urlpatterns = [


    path('signupx', views.signup, name="signupx"),
    path('home1', views.home1fun, name='home1'),
    path('home2', views.home2fun, name='home2'),
    path('home3', views.home3fun, name='home3'),
    path('adminfirstpage', views.adminfirstpage, name='adminfirstpage'),
    path('addquestion',views.addquestion,name="addquestion"),
    path('test2',views.test2fun,name="test2"),
    path('test3',views.test3fun,name="test3"),
    path('login', views.loginfun, name='login'),
    path('adminpage', views.adminhomefun, name='adminpage'),
    path('signuptable', views.signuptable, name='signuptable'),
    path('deletetable/<int:deletex>', views.deletetable, name='deletetable'),
    path('updatetable', views.updatetable, name='updatetable'),
    path('', views.homefun, name='home'),
    path('adminpage_2',views.adminpage,name='adminpage')



]
