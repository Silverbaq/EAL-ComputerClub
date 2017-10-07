from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsPost
from .forms import CommentForm


# Create your views here.
def index(request):
    posts = NewsPost.objects.all()
    return render(request, 'site/index.html', {'posts': posts})


def news_post(request, pk):
    post = get_object_or_404(NewsPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('news_post', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'site/post.html', {'post': post, 'form': form})