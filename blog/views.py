from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import EmailPostForm
from .models import Post
from .forms import EmailPostForm
# Create your views here.


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# def post_list(request):
#     posts_list = Post.published.all()
#     paginator = Paginator(posts_list, 3)
#     page_number = request.GET.get('page', 1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'blog/post/list.html',
#                   {'posts':posts})


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No post found')
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'post': post, 'form': form})
