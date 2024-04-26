from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    Names = [
        {'name':'Lokesh More','age':23},
        {'name':'Rohit Hadashi','age':23},
        {'name':'Yash Hadashi','age':17},
        {'name':'Jay Panchal','age':18},
        {'name':'Tahir bro','age':27}
    ]
    vegetables = ['Pumpkin','Tomato','Potato','']
    return render(request, "html/index.html",context = {'Names':Names,'vegetables':vegetables,'page':'Home Page'})

def contact(request):
    context = {'page':'Contact'}
    return render(request,'html/contact.html', context )

def about(request):
    context = {'page':'About'}
    return render(request,'html/about.html', context)

def success_page(request):
    return HttpResponse("<h1>Hey this is success page.</h1>")