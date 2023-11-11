from django.shortcuts import render, get_object_or_404
from .models import Character, Equipement

def post_list(request):
    characters = Character.objects.all()
    equipements = Equipement.objects.all()
    return render(request, 'snails/post_list.html', {'characters': characters, 'equipements':equipements})


def post_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    equipement = get_object_or_404(Equipement, pk=pk)
    return render(request, 'snails/post_detail.html', {'character': character, 'equipement':equipement})