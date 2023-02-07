from venv import logger
from django.shortcuts import render, redirect
from django.views.generic.base import View
from simple_search import search_filter
from .models import Post

from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .form import CommentsForm
from .models import Post, Likes, Visit


class PostView(View):
    '''Вывод записей'''

    def get(self, request):
    
     try:
        ip = get_client_ip(request)
        '''Получаем обескт с базы, по полученому ip, якшо нема в базе то созд. новый '''
        visits = Visit.objects.get(ip_addr = ip)
        visits.count += 1
        visits.save()
        visits = Visit.objects.all()
     except:
         '''создается новый обект'''
         visit = Visit()
         visit.count += 1
         visit.ip_addr = ip
         visit.save()
         visits = Visit.objects.all()
            
     posts = Post.objects.all().order_by('-id')
     return render(request, "blog/blog.html", {'post_list': posts, 'visits': visits})

class Dostavka(View):
    '''Доставка'''
    def get(self, request):
        return render(request, "blog/dostavka.html")


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /admin",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

class PostDetail(View):
    '''отдельная страница для записи'''

    def get(self, request, pk):
        
        post = Post.objects.get(id=pk)
        post.views +=1
        post.save()
        return render(request, 'blog/blog_detail.html', {'post': post})


class AddComents(View):
    '''Добавление комментариев'''

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect('/')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
