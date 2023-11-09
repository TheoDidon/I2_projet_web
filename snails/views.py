from django.shortcuts import render, get_object_or_404
from .models import Character

def post_list(request):
    characters = Character.objects.all()
    return render(request, 'snails/post_list.html', {'characters': characters})


