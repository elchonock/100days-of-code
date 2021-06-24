from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'a first meetup', 'location': 'Kyiv', 'slug': 'a-first-meetup'},
        {'title': 'a second meetup', 'location': 'Luhansk', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })
