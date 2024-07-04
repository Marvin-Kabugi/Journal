from django.urls import path
from . import views

urlpatterns = [
    path('tag-items', views.TagList.as_view(), name='tag-list'),
    path('tag-items/<int:pk>', views.TagDetail.as_view(), name='tag-detail'),
    path('category-items', views.CategoryList.as_view(), name='category-list'),
    path('category-items/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('journal-entries', views.JournalEntryDetail.as_view(), name='journal-list'),
    path('journal-entries/<int:pk>', views.JournalEntryList.as_view(), name='journal-detail')
]