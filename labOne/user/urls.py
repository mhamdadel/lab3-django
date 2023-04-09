from django.urls import path
from . import views
urlpatterns = [
    path('list' ,views.index ),
    path('login' ,views.login_request ),
    path('register' ,views.register_request ),
    path('logout' ,views.login_request ),
]
