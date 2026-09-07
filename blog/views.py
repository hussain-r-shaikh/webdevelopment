from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.core.paginator import Paginator
from .forms import RegisterForm, CommentForm
from .models import Category, Post, Comment



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 3



def post_category(request, pk):
    post_list = Post.objects.filter(category__id=pk)

    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "index.html", {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
    })



def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            # 1. Print errors dictionary directly to terminal/console
            print("Form validation failed!")
            print(form.errors)
    else: form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})
        



def category_index(request, category):
    blogs = Post.objects.filter(category__category=category)
    return render(request,"category_index.html", {"blogs":blogs})


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


