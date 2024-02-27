from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def posts_home(request):
    posts = Articles.objects.order_by('-date')
    return render(request, 'posts/posts_home.html', {'posts': posts})


class PostsDetailView(DetailView):
    model = Articles
    template_name = 'posts/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = 'Error 202'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'posts/create.html', data)
