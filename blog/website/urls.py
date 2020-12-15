from django.urls import path, include
from .views import hello
from .views import post_detail, saveform


urlpatterns = [
   
    path('', hello, name='hello'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('save-form/', saveform, name="saveform"),

]
