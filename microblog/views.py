from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.utils import timezone
from django.db.models import Q

from microblog.models import *
from microblog.forms import *


# mikroblog about

def Microblog_about(request):
    return render(request, "microblog_about.html")


# manage posts

class PostList(ListView):
    model = Post
    template_name = "manage_posts/post_list.html"
    context_object_name = "posts"
    paginate_by = 5
    ordering = ['-created_date']

    def get_queryset(self):
        posts = Post.objects.filter(id_author__username="admin").order_by('-created_date')
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all().order_by('name')
        return context


# Comments in PostDetail without pagination

# class PostDetail(DetailView):
#     template_name = 'manage_posts/post_detail.html'
#     model = Post

#     def get_context_data(self, **kwargs):
#         post_pk = self.request.resolver_match.kwargs.get("pk")
#         context = super(PostDetail, self).get_context_data(**kwargs)
#         context['comments'] = Comment.objects.filter(post__pk=post_pk).order_by('-created')
#         return context

# Comments in PostDetail with pagination

class PostDetail(DetailView, MultipleObjectMixin):
    template_name = 'manage_posts/post_detail.html'
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        post_pk = self.request.resolver_match.kwargs.get("pk")
        comments = Comment.objects.filter(post__pk=post_pk).order_by('-created')
        context = super(PostDetail, self).get_context_data(object_list=comments, **kwargs)
        comments_number = comments.count()
        context['comments_number'] = comments_number
        return context


class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = "manage_posts/post_add.html"

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.id_author = self.request.user
        self.object.created_date = timezone.now()
        self.object.publication_date = timezone.now()
        self.object.save()
        return super().form_valid(form)

    @property
    def success_url(self):
        return reverse('Post_detail', kwargs={'pk': self.object.pk})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.id_author = request.user
            post.publication_date = timezone.now()
            post.save()

            return redirect('Post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'manage_posts/post_add.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('Post_manager')
    return render(request, 'manage_posts/post_delete.html', {'post': post})


class CommentAdd(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "manage_posts/comment_add.html"

    def form_valid(self, form, *args, **kwargs):
        post_pk = self.request.resolver_match.kwargs.get("pk")
        self.object = form.save(commit=False)
        self.object.post = Post.objects.get(pk=post_pk)
        self.object.save()
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        post_pk = self.request.resolver_match.kwargs.get("pk")
        try:
            if self.request.user.is_authenticated:
                initial["name"] = self.request.user
                initial["email"] = self.request.user.email
        except Post.DoesNotExist:
            pass
        return initial

    def get_context_data(self, **kwargs):
        post_pk = self.request.resolver_match.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.filter(pk=post_pk).first()
        return context

    @property
    def success_url(self):
        return reverse('Post_detail', kwargs={'pk': self.object.post.pk})


# user panel

class PostManager(ListView):
    model = Post
    template_name = "user_panel/post_manager.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user_name = self.request.user.username
        posts = Post.objects.filter(id_author__username=user_name).order_by('-created_date')
        return posts

    def get_context_data(self, **kwargs):
        post_pk = self.request.resolver_match.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post__pk=post_pk)
        return context


class MyMicroblog(ListView):
    model = Post
    template_name = "user_panel/my_microblog.html"
    context_object_name = "posts"
    paginate_by = 4
    ordering = ['-created_date']

    def get_queryset(self):
        user_name = self.request.resolver_match.kwargs.get("id_author")
        posts = Post.objects.filter(id_author__username=user_name).order_by('-created_date')
        return posts

    def get_context_data(self, **kwargs):
        user_name = self.request.resolver_match.kwargs.get("id_author")
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(name=user_name)[:5]
        context['user_name'] = user_name
        context['received_comments'] = Comment.objects.filter(post__id_author__username=user_name).count()
        context['written_comments'] = Comment.objects.filter(name=user_name).count()

        return context


# ranking

class Top5(ListView):
    model = Post
    template_name = "top5.html"
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-rating__average")[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = BlogCategory.objects.all().order_by("name")
        return context


# serching

class TitleContextSerching(ListView):
    model = Post
    template_name = 'manage_posts/post_searching.html'
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        query_q = self.request.GET.get("q")
        query_p = self.request.GET.get("p")
        query_r = self.request.GET.get("r")
        object_list = Post.objects.all()
        if query_q:
            object_list = object_list.filter(id_author__username__contains=query_q)
        if query_p:
            object_list = object_list.filter(
                Q(title__contains=query_p)
                | Q(short__contains=query_p)
                | Q(contents__contains=query_p)
            )
        # if query_r:
        #     object_list = object_list.filter(category__name__contains=query_r)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all().order_by('name')
        return context


class CategorySerching(ListView):
    model = Post
    template_name = 'manage_posts/post_searching.html'
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        post_category = self.request.resolver_match.kwargs.get("category")
        print(post_category)
        posts = Post.objects.filter(category__name=post_category).order_by('-created_date')
        print(posts)
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all().order_by('name')
        return context
