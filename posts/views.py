from django.shortcuts import render, redirect

from .models import Post

def index(request):
    posts = Post.objects.all()  # 모든 게시물 가져오기

    context = {
        'posts': posts  # 게시물 추가
    }
    return render(request, 'index.html', context)  # index.html 렌더링

def detail(request, id):
    post = Post.objects.get(id=id)  # 특정 id의의 게시물 가져오기

    context = {
        'post': post,  # 게시물 추가
    }
    return render(request, 'detail.html', context)  # detail.html 렌더링

def new(request):
    return render(request, 'new.html')  # new.html 렌더링

def create(request):
    title = request.GET.get('title')  # 제목 가져오기
    content = request.GET.get('content')  # 내용 가져오기
    post = Post()  # 새로운 게시물 생성
    post.title = title  # 제목 설정
    post.content = content  # 내용 설정
    post.save()  # 게시물 저장
    return redirect(f'/posts/{post.id}/')  # 상세 페이지로 리다이렉트

def delete(request, id):
    post = Post.objects.get(id=id)  # 특정 게시물 가져오기
    post.delete()  # 게시물 삭제
    return redirect('/posts/')  # 목록 페이지로 리다이렉트

def edit(request, id):
    post = Post.objects.get(id=id)  # 특정 id의의 게시물 가져오기
    context = {
        'post': post,  # 게시물 추가
    }
    return render(request, 'edit.html', context)  # edit.html 렌더링

def update(request, id):
    title = request.GET.get('title')  # 제목 가져오기
    content = request.GET.get('content')  # 내용 가져오기
    post = Post.objects.get(id=id)  # 특정 id의의 게시물 가져오기
    post.title = title  # 제목 설정
    post.content = content  # 내용 설정
    post.save()  # 게시물 저장
    return redirect(f'/posts/{post.id}/')  # 상세 페이지로 리다이렉트

def temp(request):
    return redirect('/posts/') # posts/로 리다이렉트