from django.shortcuts import render

def hom_page(request):
    return render(request, 'index.html')


