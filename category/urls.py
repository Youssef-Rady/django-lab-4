from django.urls import path
from category.views import AllCategories, CreateCategory, CategoryListView, CategoryCreateView, CategoryDetailedView, CategoryUpdateView, CategoryDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
   # path('', AllCategories.as_view(), name='categories.index'),
   # path('create', CreateCategory.as_view(), name='categories.create'),
   path('', CategoryListView.as_view(), name='categories.index'),
   path('create', CategoryCreateView.as_view(), name='categories.create'),
   path('<int:pk>', CategoryDetailedView.as_view(), name='categories.show'),
   path('<int:pk>/edit', login_required(CategoryUpdateView.as_view()), name='categories.edit'),
   path('<int:pk>/delete', CategoryDeleteView.as_view(), name='categories.delete'),
]