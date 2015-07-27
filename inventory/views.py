from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, DetailView, CreateView
from .models import Inventory
from .forms import InventoryForm

# class InventoryIndex(ListView):
# 	model = Inventory
# 	template_name = "index.html"

# class InventoryDetail(DetailView):
# 	model = Inventory
# 	template_name = "detail.html"

# class InventoryAdd(CreateView):
# 	model = Inventory
# 	template_name = "new.html"

def index(request):
	items = Inventory.objects.all()
	form = InventoryForm()
	if request.GET:
		groupby = request.GET.get("groupby")
		return render_to_response("inventory/index_results.html", {'items': items,
												 'groupby': groupby})
	else:
		groupby = "name"
		return render(request, "inventory/index.html", {'items': items,
											  'groupby': groupby,
											  'form': form})

def add(request):
	if request.method == "POST":
		form = InventoryForm(request.POST)
		print("post")
		if form.is_valid():
			print("valid")
			form.save(commit=True)
			return render_to_response("inventory/index_adddiv.html",
							  {'form': form})
		else:
			print(form.errors)
	else:
		form = InventoryForm()
		return render_to_response("inventory/index_adddiv.html",
							  {'form': form})