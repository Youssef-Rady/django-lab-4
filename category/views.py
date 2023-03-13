from django.shortcuts import render, redirect
from django.views import View
from category.models import Category
from category.forms import CategoryModelForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class AllCategories(View):
    def get(self, request):
        category = Category.get_all_categories()
        return render(request, 'category/index.html', context={'category': category})
    
class CreateCategory(View):
    def get(self, request):
        categoryform = CategoryModelForm()
        return render(request, 'category/create.html', context={'form': categoryform})
    def post(self, request):
        categoryform = CategoryModelForm(request.POST, request.FILES)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('categories.index')
        return redirect('categories.create')
    
class CategoryListView(ListView):
    model = Category
    template_name = 'category/index.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category/create.html'
    form_class = CategoryModelForm
    success_url = '/categories/'

class CategoryDetailedView(DetailView):
    model = Category
    template_name = 'category/show.html'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category/edit.html'
    form_class = CategoryModelForm
    success_url = '/categories/'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/delete.html'
    success_url = '/categories/'