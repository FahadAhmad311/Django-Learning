from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def items(request):
    dishes = [
        {'dish': 'Russian Salad', 'sauce': 'Chillie Sauce'},
        {'dish': 'Biryani', 'sauce': 'Raita'},
        {'dish': 'Zinger Burger', 'sauce': 'Ketchup'}
    ]
    return render(request, 'items.html', {'dishes': dishes})