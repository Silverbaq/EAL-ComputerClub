from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsPost
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = NewsPost.objects.all().order_by('-id')
    return render(request, 'site/index.html', {'posts': posts})


def news_post(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'site/post.html', {'post': post, 'comments':comments, 'form': form})


@login_required
def comment(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_by = request.user
            comment.save()
            return redirect('news_post', pk=pk)
    return render(request, 'site/news_post', pk=pk)

