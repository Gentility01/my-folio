from datetime import datetime
from itertools import product
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Folio_Blog, Comments  #,ReplyingComent
from .forms import COmmentForm  #, ReplyComent
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

@login_required(login_url='login_view')
def blog_view(request):
    blog = Folio_Blog.objects.all().order_by('-datecreated')
    blog_paginator = Paginator(blog,10)
    page_num = request.GET.get('page')
    page = blog_paginator.get_page(page_num)
    
    context = {
        'page':page
    }
    return render(request,'blogs/blogs.html', context)

@login_required(login_url='login_view')
def blog_detail(request, id ):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    search_blog = Folio_Blog.objects.filter(Q(title__icontains=q))
    details = get_object_or_404(Folio_Blog, id=id)
    recent =  Folio_Blog.objects.all().order_by('-datecreated')
    b = Paginator(recent,2)
    recent_pages = b.get_page(1)
    
    form = COmmentForm(instance=details)
    if request.method == 'POST':
        form = COmmentForm(request.POST,instance=details )
        if form.is_valid():
            name =request.user
            body = form.cleaned_data['comment_body']
            comment_model = Comments(blog_comment=details, commenter_name=name, comment_body=body, date_added=datetime.now())
            comment_model.save()
            return redirect('blog_detail', id)
        else:
            print('invalid form')
    else:
        form = COmmentForm()

    context= {
        'details':details,
        'recent_pages':recent_pages,
        'recent':recent,
        'form':form,
        'search_blog':search_blog
        # 'reply_comment_detail':reply_comment_detail,
        # 'reply_form_detail':reply_form_detail
    }
    return render(request, 'blogs/blog_details.html', context)


# def reply_comment(request, id):
#     reply_comment_details = get_object_or_404(Comments, id=id)
#     reply_form = ReplyComent(instance=reply_comment_details)
#     if request.method == 'POST':
#         reply_form = ReplyComent(instance=reply_comment_details)
#         if reply_form.is_valid():
#             name =request.user
#             body = reply_form.cleaned_data['comment_body']
#             reply_model = ReplyingComent(comment_on = reply_comment_details, r_name=name, comment_body=body, date_added=datetime.now())
#             reply_model.save()
#             return redirect('blog_detail', id)
#         else:
#             print('invalid form')
#     else:
#         reply_form = ReplyComent()
       
#     return render(request, 'blogs/reply_comment.html', {'reply_form':reply_form})
    
    

