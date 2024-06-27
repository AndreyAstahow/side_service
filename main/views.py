from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class IndexView(TemplateView):  
    template_name = 'main/index.html'
    
class PersonalCab(LoginRequiredMixin, TemplateView):
    template_name = 'lc/lc.html'

class MonitoringView(LoginRequiredMixin, TemplateView):
    template_name = 'monitoring/monitoring.html'

class PostView(ListView):
    model = Post
    template_name = 'monitoring/post.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    # permission_required = ('NewsPortal.add_post')
    form_class = PostForm
    model = Post
    template_name = 'monitoring/post_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostCreate, self).form_valid(form)
    
class PostDetail(DetailView):
    model = Post
    template_name = 'monitoring/post_detail.html'
    context_object_name = 'post'

    # def get_object(self, *args, **kwargs):
    #     obj = cache.get(f'post-{self.kwargs["pk"]}', None)
    #     if not obj:
    #         obj = super().get_object(queryset=self.queryset)
    #         cache.set(f'post-{self.kwargs["pk"]}', obj)
    #     return obj

class PostDelete(DeleteView):
    model = Post
    template_name = 'monitoring/post_delete.html'
    success_url = reverse_lazy('post_list')