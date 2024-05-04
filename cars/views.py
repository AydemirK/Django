from datetime import datetime
import random
from django.db.models import Q
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView , UpdateView
from cars.form import PostForm, ReviewForm, SearchForm
from cars.models import Post
from user.models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required




class MainView(View):
    def get(self, request):
        now = datetime.now()
        
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

        context = {
            'current_date_time': formatted_now
        }
        return render(request, 'main.html', context)


    
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello! It's my project")
    


class FunView(View):
    def get(self,request):
        if request.method == 'GET':
            anecdotes = [
                "Если у вас закончилась мазь от зуда,\n — Не спешите выбрасывать тюбик.\n Его уголком очень удобно чесаться.",
                "Бармен спрашивает пьяного посетителя:\n— Я вижу, у вас пустой стакан. Не хотите ли еще один?\nА на хрена мне два пустых стакана?",
                "Дорогой, ты с чем картошечку будешь на ужин?\n— С мясом.\nЯ как знала и купила чипсы с беконом."
            ]
            anecdote = random.choice(anecdotes)
            return HttpResponse(anecdote)



class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'cars/post_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        tags = self.request.GET.getlist('tags')

        posts = Post.objects.all().prefetch_related('tags')

        if search:
            posts = posts.filter(
                Q(brand__icontains=search) | Q(text__icontains=search)
            )
        
        if tags:
            posts = posts.filter(tags__id__in=tags).distinct()


        return posts

    def get(self, request, *args, **kwargs):
        search_form = SearchForm(request.GET)
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        context['search_form'] = search_form
        return self.render_to_response(context)




class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'cars/post_create.html'
    success_url = '/posts/'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'cars/post_update.html'
    pk_url_kwarg = 'post_id'
    success_url = '/posts/'

    
class AddReviewView(View):
    def get(self, request, post_id):
        
        post = Post.objects.get(id=post_id)
        form = ReviewForm()
        
        form.user = request.user
        
        return render(request, 'cars/add_review.html', {'form': form, 'post': post})

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = ReviewForm(request.POST)
        form.user = request.user
        
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            
            review.save()
            return redirect('post_detail_view', post_id=post_id)
        return render(request, 'cars/add_review.html', {'form': form, 'post': post}) 