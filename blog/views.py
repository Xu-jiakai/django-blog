from django.shortcuts import render
from . import models
from blog.forms import CommentForm
from django.http import Http404

'''
主页
'''


def index(request):
    blogs = models.Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs': blogs})






'''
博客编辑页面
'''


def edit_page(request, blog_id):
    if blog_id == '0':
        return render(request, 'blog/post.html')
    blog = models.Blog.objects.get(pk=blog_id)
    return render(request, 'blog/post.html', {'blog': blog})


'''
博客编辑响应
'''


def edit_action(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    content = request.POST.get('content')
    blog_id = request.POST.get('blog_id', '0')

    if blog_id == '0':
        models.Blog.objects.create(title=title, author=author, content=content)
        blogs = models.Blog.objects.all()
        return render(request, 'blog/index.html', {'blogs': blogs})

    blog = models.Blog.objects.get(pk=blog_id)

    blog.title = title
    blog.author = author
    blog.content = content
    blog.save()

    return render(request, 'blog/detail.html', {'blog': blog})


'''
博客内容页
评论响应
'''
def get_details(request, blog_id):
    try:
        blog = models.Blog.objects.get(id=blog_id)
    except models.Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            models.Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog/detail.html', ctx)
'''
关于我
'''
def aboutMe(request):
    return render(request,'blog/aboutMe.html')