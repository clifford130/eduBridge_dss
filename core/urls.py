from django.urls import path
from .views import HomePageView, signup

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', signup, name='signup'),
]
