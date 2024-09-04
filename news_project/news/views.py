from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .forms import PostForm
from .filters import PostFilter

def news_list(request):
    news = Post.objects.filter(type='news')
    paginator = Paginator(news, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news_list.html', {'page_obj': page_obj})

def news_search(request):
    news_list = Post.objects.filter(type='news')
    news_filter = PostFilter(request.GET, queryset=news_list)
    return render(request, 'news_search.html', {'filter': news_filter})

class ArticleCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.add_article'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'article'
        return super().form_valid(form)

class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.change_article'

class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.add_post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'news'
        return super().form_valid(form)

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.change_post'

class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = 'news.delete_post'

class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(type='news')

def news_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.type = 'news'
            news.save()
            return redirect('news_list')
    else:
        form = PostForm()
    return render(request, 'news_form.html', {'form': form})


def news_edit(request, pk):
    news = get_object_or_404(Post, pk=pk, type='news')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = PostForm(instance=news)
    return render(request, 'news_form.html', {'form': form})

def news_delete(request, pk):
    news = get_object_or_404(Post, pk=pk, type='news')
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'news_confirm_delete.html', {'news': news})
