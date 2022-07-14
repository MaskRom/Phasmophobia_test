from django.utils import timezone
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .forms import activate_user
from django.http import HttpResponse
from .forms import SignUpForm

from .models import Post, Favorite




class index_view(ListView):
    model = Post
    template_name = "registration/index.html"


    def get_queryset(self, **kwargs):
        login_user = self.request.user
        queryset = super().get_queryset(**kwargs)
        #queryset = queryset.filter(user=login_user) 
        #queryset = queryset.all()
        return queryset
"""
    def get_context_data(self, **kwargs):
        login_user = self.request.user
        context = super().get_context_data(**kwargs)
        context["favo"] = Favorite.objects.filter(target=8)[0].target
        return context
"""
class post_view(CreateView):
    model = Post
    template_name = "post.html"
    success_url = reverse_lazy('app:index')
    fields = '__all__'
    



def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id)
        m = Favorite(user = request.user, target=likedpost)
        n = Favorite.objects.filter(target=likedpost, user = request.user)
        if n:
            n.delete()
            return HttpResponse('false')
        else:
            m.save()
            return HttpResponse('true')
    else:
        return HttpResponse("unsuccesful")


    

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)