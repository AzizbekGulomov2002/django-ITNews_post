from django.shortcuts import render


from app.models import Post
from .models import Post

def main(request):
    if request.method=="POST":
        search = request.POST['qidiruv']
        posts = Post.objects.filter(malumot__icontains=search)
        return render(request,'blog/search.html',{"posts":posts})  
    post = Post.objects.all()
    return render(request,'blog/basic.html',{"posts":post})



def post_detail(request,id):    
    posts=Post.objects.get(id=id)
    posts.kurishlar=posts.kurishlar+1
    posts.save()
    return render(request,'blog/post_detail.html',{"posts":posts})




