from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'user_text': user_text, 'user_reversed_text': reversed_text})
