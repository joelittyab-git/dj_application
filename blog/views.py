from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BlogPostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import JsonResponse

# Create your views here.
def home_view(request):
    
    posts = Post.objects.all().reverse()
    
    # data = db.get()
    # return JsonResponse(data, safe=False)
    
    return render(
        request,
        template_name='blog.html',
        context={
            'name':'Home',
            'posts': posts.reverse(),
        }
    )
    
def post_blog_view(request):
    if(request.method == 'GET' and request.user.is_authenticated == False):
        messages.warning(request, 'You must be logged in to post a blog')
        return redirect('user-login')
    elif(request.method == 'POST'):
        form = BlogPostForm(request.POST)
        if(form.is_valid()):
            posted_data = form.save(commit=False)
            posted_data.author = request.user
            posted_data.save()
            messages.success(request, 'Blog has been posted successfully')
            return redirect('blog-home')
        
        else:
            return render(
                request=request,
                template_name='blog-post.html',
                context={
                    'form': form,
                    'name':'My Blog'
                }
            )
    
    #On get request
    form = BlogPostForm()    
    return render(
        request=request,
        template_name='blog-post.html',
        context={
            'form': form,
            'name':'My Blog'
        }
    )
    
    
def handler_404(request, exception):
    return render(
        template_name='404.html'
    )
    
