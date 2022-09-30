from multiprocessing import context
from django.shortcuts import redirect, render

from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def new(request):
    return render(request, "reviews/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    updated_at = request.GET.get("updated_at")
    Review.objects.create(
        title=title, content=content, created_at=created_at, updated_at=updated_at
    )
    # context = {
    #     "title": title,
    #     "content": content,
    #     "created_at": created_at,
    #     "updated_at": updated_at,
    # }

    return redirect("reviews:index")


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/edit.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    updated_at = request.GET.get("updated_at")

    review.title = title
    review.content = content
    review.created_at = updated_at
    review.created_at = created_at
    review.save()

    return redirect("reviews:detail", review.pk)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")
