from django.shortcuts import render, get_object_or_404
from .models import Character

def post_list(request):
    characters = Character.objects.all()
    return render(request, 'snails/post_list.html', {'characters': characters})


def post_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    return render(request, 'snails/post_detail.html', {'character': character})