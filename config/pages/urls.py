from django.urls import path
# from .views import homePageView, djangoView,contactView,about
from .views import *
urlpatterns = [
   # path('home/', homePageView, name='home'),
   # path('django/', djangoView, name='django'),
   # path('contact/',contactView,name='contact'),
   # path('about/',about,name='contact'),
   # path('', HomePageView.as_view(), name='home'),
   #path('about/', AboutPageView.as_view(), name='about'),
   #path('contact/', ContactPageView.as_view(), name='contact'),
   path('home/', home, name='home'),
   path('about/', about, name='about'),

  
   
]