from django.urls import path,include
from .views import index,SignUp
#remember this login logout
from django.contrib.auth import urls
urlpatterns = [
    path('',index,name="index"),
    path('',include('django.contrib.auth.urls')),
    path('signup/',SignUp.as_view(),name="signup"),
]
