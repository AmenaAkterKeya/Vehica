from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def car_brand(request):
    if request.method=='POST':
        brandName=forms.BrandForm(request.POST)
        if brandName.is_valid():
            brandName.save()
            return redirect(car_brand)
        
    else:
        brandName=forms.BrandForm()
    return render(request,'brand.html',{'form':brandName})