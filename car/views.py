
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from . import forms
from . import models
from django.contrib import messages
from author.models import Order

@login_required
def sell_car(request):
    if request.method=='POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.instance.author = request.user
            car_form.save()
            return redirect(sell_car)
    else:
        car_form = forms.CarForm()
        return render(request,'sellCar.html',{'form': car_form})

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'sellCar.html'
    success_url = reverse_lazy('sell_car')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
@login_required
def edit_car(request, id):
    car = models.Car.objects.get(pk=id) 
    car_form = forms.CarForm(instance=car)
    
    if request.method == 'POST': 
        car_form = forms.CarForm(request.POST, instance=car) 
        if car_form.is_valid():
            car_form.instance.author = request.user
            car_form.save()
            return redirect('homepage')
    
    return render(request, 'sellCar.html', {'form' : car_form})
@login_required
def delete_car(request, id):
    car = models.Car.objects.get(pk=id) 
    car.delete()
    return redirect('homepage')

class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'carDetails.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context  
# @login_required
# def buy_car(request, id):
#     car = models.Car.objects.get(pk=id)
#     if car.quantity > 0:
#         car.quantity -= 1
#         car.save()
#         return redirect('detail_car', id=car.id)
@login_required
def car_view(request, id):
    car = models.Car.objects.get(pk=id)

    if car.quantity > 0:
        Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
        messages.success(request, 'Car bought successfully!')
    else:
        messages.error(request, 'Car out of stock!')
    return redirect('detail_car', id=car.id)

            
            
