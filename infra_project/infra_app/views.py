from django.http import HttpResponse


def index(request):
    return HttpResponse('у меня получилось!')


def second_page(request):
    return HttpResponse('а это вторая страница')
