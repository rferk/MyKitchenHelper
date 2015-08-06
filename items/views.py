from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, DetailView, CreateView
from django.forms.models import modelformset_factory
from .models import Item
from .forms import ItemForm

def index(request):
	items = Item.objects.all()
	groupby = "name"
	return render(request, 
				  "inventory/index.html", 
				  {'items': items, 'groupby': groupby})

def regroup(request):
	items = Item.objects.all()
	groupby = request.GET.get("groupby")
	return render_to_response("inventory/index_results.html", 
							  {'items': items, 'groupby': groupby})


def new(request):
	items = Item.objects.all()
	groupby = "name"
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			form.save()
			form = ItemForm()
	else:
		form = ItemForm()
	return render(request, 
				  "inventory/new.html", 
				  {'items': items, 'groupby': groupby, 'form': form})

def edit(request):
	ItemFormSet = modelformset_factory(
		Item, 
		fields=('name', 'category', 'stock', 'tracked', 'threshold'),
		extra=0
	)
	if request.method == "POST":
		formset = ItemFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
			return redirect("inventory:index")
	else:
		formset = ItemFormSet()
	return render(request, "inventory/edit.html", {"formset": formset})