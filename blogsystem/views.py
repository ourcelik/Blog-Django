import json
from django.http.response import Http404, HttpResponse, HttpResponseRedirect, HttpResponseRedirectBase
from .models import Comment, Post
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.core.paginator import Paginator
from json import dumps
from django.core import serializers
from django.urls import reverse
from .forms import CommentForm
from django.contrib import messages


def index(request):
    context = {
        'posts': Post.objects.order_by('-date_posted')[:6],
        'Csharp_Posts': Post.objects.filter(header="C-Sharp").order_by('?')[:6],
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = request.POST.get('comment')
            name = request.POST.get('name')
            form = Comment(content=comment, name=name, post=post)
            form.save()
            messages.success(request, 'Successful process')
            return HttpResponseRedirect('.')
    else:
        form = CommentForm()
        context = {
            'post': post,
            'CommentForm': form,

        }
        return render(request, 'blog/post_detail.html', context)


class CommentCreateView(CreateView):
    model = Comment
    fields = ["content", ]
    template_name = "blog/create_comment.html"

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse('post-detail', kwargs={'slug': self.kwargs['slug'], })


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


class PortfolioView(TemplateView):
    template_name = 'blog/cv.html'


class AboutView(TemplateView):
    template_name = 'blog/about_me.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/postlist.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class RandomPostByHeader:
    def Csharp(self, request):
        ct_json = self.PreProcess('C-Sharp')
        return HttpResponse(ct_json, content_type="application/json")

    def Css(self, request):
        ct_json = self.PreProcess('Css')
        return HttpResponse(ct_json, content_type="application/json")

    def Javascript(self, request):
        ct_json = self.PreProcess('Javascript')
        return HttpResponse(ct_json, content_type="application/json")

    def Python(self, request):
        ct_json = self.PreProcess('Python')
        return HttpResponse(ct_json, content_type="application/json")

    def Html(self, request):
        ct_json = self.PreProcess('Html')
        return HttpResponse(ct_json, content_type="application/json")

    def PreProcess(self, header):
        ct = Post.objects.filter(header=f"{header}").order_by('?')[:6]
        ct_json = serializers.serialize('json', ct)
        return ct_json
