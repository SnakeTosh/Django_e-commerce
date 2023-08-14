from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item
from django.contrib.auth.models import User

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request,  'dashboard/index.html', {
        'items': items,
    })
    

def seller(request, pk):
    user = User.objects.get(pk=pk)
    items = Item.objects.filter(created_by=pk)
    return render(request, 'item/seller.html', {
        'user':user,
        'items':items,
    })