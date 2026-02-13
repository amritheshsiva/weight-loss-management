from django.shortcuts import render, redirect
from .forms import WeightForm,WeightEditForm,DateRangeForm
from .models import Weight
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# To add weight
@login_required
def add_weight(request):
    if request.method == 'POST':
        form = WeightForm(request.POST)
        if form.is_valid():
            today = date.today()
            already_added = Weight.objects.filter(user=request.user,date=today).exists()
            if already_added:
                messages.error(request, "You have already added weight today.")
            else:
                Weight.objects.create(
                    user=request.user,
                    weight=form.cleaned_data['weight']
                )
                messages.success(request, "Weight added successfully.")
                return redirect('weight_list')
    else:
        form = WeightForm()
    return render(request, 'add_weight.html', {'form': form})

# To show Weight List
@login_required
def weight_list(request):
    weight_objects = Weight.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(weight_objects, 1) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weight_list.html', {'page_obj': page_obj})

# To delete Weight
from django.shortcuts import get_object_or_404
@login_required
def delete_weight(request, id):
    weight = get_object_or_404(Weight, id=id, user=request.user)
    weight.delete()
    return redirect('weight_list')

# To edit Weight
@login_required
def edit_weight(request, id):
    weight_obj = get_object_or_404(Weight, id=id, user=request.user)
    if request.method == 'POST':
        form = WeightEditForm(request.POST)
        if form.is_valid():
            weight_obj.weight = form.cleaned_data['weight']
            weight_obj.save()
            return redirect('weight_list')
    else:
        form = WeightEditForm(initial={'weight': weight_obj.weight})
    return render(request, 'edit_weight.html', {'form': form})

# Weight Difference
@login_required
def weight_difference(request):
    result = None
    form = DateRangeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        start = form.cleaned_data['start_date']
        end = form.cleaned_data['end_date']

        weights = Weight.objects.filter(
            user=request.user,
            date__range=(start, end)
        ).order_by('date')
        if weights.exists():
            start_weight = weights.first().weight
            end_weight = weights.last().weight
            result = start_weight - end_weight
    return render(request, 'weight_difference.html', {
        'form': form,
        'result': result
    })
