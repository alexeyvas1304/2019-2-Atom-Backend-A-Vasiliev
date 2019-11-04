from django.shortcuts import render
from django.http import HttpResponseNotAllowed


def common(request):
    if request.method == 'GET':
        return render(request, 'common.html')
    return HttpResponseNotAllowed(request.method)
