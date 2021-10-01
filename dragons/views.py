from django.shortcuts import render
from .dragon import Dragon
from .dragon import calculate_breeds

def index(request):
    return render(request, 'dragons/index.html')

def calculate(request):
    try:
        strength1 = int(request.POST['strength1'])
        cunning1 = int(request.POST['cunning1'])
        resistance1 = int(request.POST['resistance1'])
        eggs1 = int(request.POST['eggs1'])

        strength2 = int(request.POST['strength2'])
        cunning2 = int(request.POST['cunning2'])
        resistance2 = int(request.POST['resistance2'])
        eggs2 = int(request.POST['eggs2'])

    except(KeyError,ValueError):
        return render(request,'dragons/index.html',{'error_message':"No llenastes todos los campos de manera correcta"})
    else:
        random_numbers = [x for x in range(1,7)]
        dragon1 = Dragon(strength1,cunning1,resistance1,eggs1)
        dragon2 = Dragon(strength2,cunning2,resistance2,eggs2)

        if dragon1.rarity != 'rare' and dragon2.rarity != 'rare':
            values = calculate_breeds(dragon1,dragon2)
            return render(request,'dragons/index.html',{'dragons':values['dragon_list'],'cyt':values['cyt'] ,'nums':random_numbers})
        else:
            return render(request,'dragons/index.html',{'error_message':"No puedes hacer breed con dragones raros"})