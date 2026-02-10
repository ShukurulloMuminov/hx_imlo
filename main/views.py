from django.shortcuts import render
from .models import *


def index_view(request):
    togri = None
    notogrilar = None
    message = None

    search = request.GET.get('search')
    if search:
        search = search.lower()
        togrilar = Togri.objects.filter(soz=search)
        if togrilar.exists():
            togri = togrilar.first()
            notogrilar = Notogri.objects.filter(togri=togri)
        else:
            notogrilar = Notogri.objects.filter(soz=search)
            if notogrilar.exists():
                notogri = notogrilar.first()
                togri = notogri.togri
                notogrilar = togri.notogri_set.all()
            else:
                if 'h' not in search and 'x' not in search:
                    message = "Bu so'zda Hh va Xx ishtirok etmagan"
                elif not search.isalpha():
                    message = "Notog'ri kiritish!"
                else:
                    message = "Bu so'z bazamizda yo'q"



    context = {
        'message': message,
        'search': search,
        'togri': togri,
        'notogrilar': notogrilar}


    return render(request, 'index.html', context)
