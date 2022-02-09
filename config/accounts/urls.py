from unicodedata import name
from django.urls import path
from .views import SignUpView ,passwordchange , passwordreset
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', passwordchange, name='password_change'),
    path('password_reset/', passwordreset, name='password_reset'),
    # path('profile/', profile, name='profile'),
]