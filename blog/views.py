from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    all_posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    print(all_posts)
    return render(request, 'blog/post_list.html', {'all_posts':all_posts})


    