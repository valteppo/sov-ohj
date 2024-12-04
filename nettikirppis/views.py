from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Item, Comment
from .forms import ItemForm, CommentForm

# Create your views here.
def check_owner(item, user, request):
    #checks if right user
    if item.owner!=request.user:
        raise Http404

def index(request):
    return render(request, 'nettikirppis/index.html')

@login_required
def items(request):
    items = Item.objects.order_by('date_added')
    context = {'items':items}
    return render(request, 'nettikirppis/items.html', context)

@login_required
def item(request, item_id):
    item = Item.objects.get(id=item_id)
    comments = item.comment_set.order_by('date_added')
    context = {'item':item, 'comments':comments}
    return render(request, 'nettikirppis/item.html', context)

@login_required
def new_item(request):
    if request.method != 'POST':
        form = ItemForm()
    else:
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('nettikirppis:items')
    
    context = {'form':form}
    return render(request, 'nettikirppis/new_item.html', context)

@login_required
def new_comment(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.item = item
            new_comment.save()
            return redirect('nettikirppis:item', item_id=item_id)
    
    context = {'item':item, 'form':form}
    return render(request, 'nettikirppis/new_comment.html', context)

@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    item = comment.item

    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('nettikirppis:item', item_id = item.id)
    
    context = {'comment':comment, 'item':item, 'form':form}
    return render(request, 'nettikirppis/edit_comment.html', context)

