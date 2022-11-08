from django.shortcuts import render
from testApp.forms import Cart


# Create your views here.
def cart_view(request):
    f1=Cart()
    if request.method == 'POST':
        name = request.POST['Name']
        quantity = request.POST['Quantity']
        # name = request.GET['Name']
        # request.session["name"]=name
        # quantity=request.GET['Quantity']
        # request.session["quantity"]=quantity
        request.session[name] = quantity

    return render(request, 'app1/add.html',{'form1': f1})


def display_view(request):
    return render(request, 'app1/display.html')