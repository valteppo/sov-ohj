from django.urls import path

from . import views

app_name = 'nettikirppis'
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('items/<int:item_id>', views.item, name='item'),
    path('new_item/', views.new_item, name='new_item'),
    path('new_comment/<int:item_id>/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),

]