from django import forms


class Cart(forms.Form):
    Name = forms.CharField()
    Quantity = forms.IntegerField()



