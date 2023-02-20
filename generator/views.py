from django.shortcuts import render
from django.http import HttpResponse
import secrets
import string
# Create your views here.

#Home Page
def home(request):
    return render(request, "generator/home.html")


#passwordgenerationPage
def passGenPage(request):
    # the password randomg generator logic
    char = string.ascii_lowercase
    
    #conditions
    if request.GET.get('uppercase'):
        char += string.ascii_uppercase
    if request.GET.get('special'):
        char += string.punctuation
    if request.GET.get('numbers'):
        char += string.digits
    
    n = int(request.GET.get('range', 12))
    genPass = ''
    for ran in range(n):
        genPass += secrets.choice(char)

    return render(request, "generator/passGenPage.html", {'password': genPass})



#about Page
def about(request):
    return render(request, "generator/about.html")