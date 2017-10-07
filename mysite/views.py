from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsPost
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    posts = NewsPost.objects.all()
    return render(request, 'site/index.html', {'posts': posts})


def news_post(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    form = CommentForm()
    return render(request, 'site/post.html', {'post': post, 'form': form})


@login_required
def comment(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('site/news_post', pk=pk)

