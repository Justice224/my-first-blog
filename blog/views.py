from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('damn')

def post_list(request):
    return render(request, 'blog/post_list.html', {})