from django.urls import path
from app.views import *

urlpatterns = [
  path('', login,  name= "login"),
  path('index', index, name= "index"),
  path('signup', signup,  name= "signup"),
  path('logout', logout,  name= "logout"),
  path('shop', shop,  name= "shop"),
  path('frieren', frieren,  name= "frieren"),
  path('naruto1', naruto1,  name= "naruto1"),
  path('naruto2', naruto2,  name= "naruto2"),
  path('jujutsu1', jujutsu1,  name= "jujutsu1"),
]
