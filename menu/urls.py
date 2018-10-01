from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.detail, name='form'),
    path('save/', views.save, name='save'),
    path('<int:item_id>/item_detail/', views.item_detail, name='item_detail'),
    path('<int:item_id>/edit_save/', views.edit_save, name='edit_save'),
    path('<int:item_id>/delete', views.delete, name='delete'),
    path('<int:item_id>/edit', views.edit, name='edit'),
]
