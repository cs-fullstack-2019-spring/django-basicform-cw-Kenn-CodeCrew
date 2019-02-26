from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Account


# Create your views here.
def index(request):
    return render(request, 'accountApp/index.html')


def welcome(request):
    print(request.POST)

    allDataEntries = Account.objects.all()

    context = {
        'name': request.POST['username'],
        'allAccounts': allDataEntries,
    }
    return render(request, 'accountApp/welcome.html', context)


def add5(request,accountID):
    clickedEntry = get_object_or_404(Account, pk=accountID)
    clickedEntry.checking += 5
    clickedEntry.save()

    allEntries = Account.objects.all()

    context = {
        'name': "New Kenn",
        'allAccounts': allEntries,
    }

    return render(request, 'accountApp/welcome.html', context)
