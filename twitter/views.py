from django.shortcuts import render

# Create your views here.


def tweets_list(request):
    return render(request, 'twitter/tweets_list.html', {})

