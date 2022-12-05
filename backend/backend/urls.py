from django.urls import path
from . import views
urlpatterns = [
path('users/',views.signin, name='signin'),
path('users/',views.signup, name='signup'),
path('users/',views.profile, name='profile'),
]