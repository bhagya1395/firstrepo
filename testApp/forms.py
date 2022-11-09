from django import forms


class Cart(forms.Form):
    Name = forms.CharField()
    Quantity = forms.IntegerField()



class Checkout(forms.Form):
    Last_name = forms.CharField()
