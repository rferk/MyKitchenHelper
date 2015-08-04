from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, DetailView, CreateView
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
	return render(request, "inventory/edit.html", {})