from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm

@login_required
def index(request):
	recipes = Recipe.objects.all()
	groupby = "name"
	return render(request, 
				  "recipes/index.html", 
				  {'recipes': recipes, 'groupby': groupby})

@login_required
def regroup(request):
	recipes = Recipe.objects.all()
	groupby = request.GET.get("groupby")
	return render_to_response("recipes/index_results.html", 
							  {'recipes': recipes, 'groupby': groupby})


@login_required
def new(request):
	recipes = Recipe.objects.all()
	groupby = "name"
	if request.method == "POST":
		form = RecipeForm(request.POST)
		if form.is_valid():
			form.save()
			form = RecipeForm()
	else:
		form = RecipeForm()
	return render(request, 
				  "recipes/new.html", 
				  {'recipes': recipes, 'groupby': groupby, 'form': form})

@login_required
def edit(request):
	return render(request, 
				  "recipes/edit.html", 
				  {})