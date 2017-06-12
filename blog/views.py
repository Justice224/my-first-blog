from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.
from django.utils import timezone
def index(request):
    return HttpResponse('damn')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {
        'posts':posts
    }
    return render(request, 'blog/post_list.html',context)