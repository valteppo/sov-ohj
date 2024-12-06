from django.urls import path

from . import views

# Image handling
from django.conf import settings
from django.conf.urls.static import static

app_name = 'nettikirppis'
urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('items/<int:item_id>', views.item, name='item'),
    path('new_item/', views.new_item, name='new_item'),
    path('new_comment/<int:item_id>/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('owner_items/', views.owner_items, name='owner_items'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('new_reply/<int:comment_id>/', views.new_reply, name='new_reply'),

    
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)