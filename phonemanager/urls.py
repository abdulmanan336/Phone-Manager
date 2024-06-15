from django.contrib import admin
from django.urls import path
from phone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('signout', views.signout,name='signout'),
    path('', views.main, name='main'),
    path('add', views.add, name='add'),
    path('form',views.form,name='form'),
    path('del/<id>',views.del_contact, name='del'),
    path('view/<id>', views.view,name='view'),
    # path('edit/<id>', views.edit,name='edit'),
    path('search', views.search,name='search'),
    path('user', views.user,name='user'),
]
