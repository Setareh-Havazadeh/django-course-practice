from django.shortcuts import render

def bloghome_view(request):
    return render(request, "blog/blog-home.html")

def blogsingle_view(request):
    return render(request, "blog/blog-single.html")
