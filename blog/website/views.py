from django.shortcuts import render
from .models import Post
from .models import Contact

def hello(request):
    lista = ['Django', 'Python','Git', 'Banco de dados', 'Linux']
    list_posts = Post.objects.filter(deleted=False)
    data = {'name': 'Curso de Django 3', 'lista_tecnologias': lista, 'posts':  list_posts}    
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post } )

def saveform(request):
   name =  name=request.POST['name']
   Contact.objects.create(
       name=name,
       email=request.POST['email'],
       message=request.POST['message'],
   )
   return render(request, 'saveform.html', {'name': name})
