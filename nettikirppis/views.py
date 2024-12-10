from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse

from .models import Item, Comment, Reply
from .forms import ItemForm, CommentForm, ReplyForm


# Create your views here.
def check_owner(item, user, request):
    #checks if right user
    if item.owner!=request.user:
        raise Http404

def index(request):
    return render(request, 'nettikirppis/index.html')

def items(request):
    items = Item.objects.order_by('date_added')
    context = {'items':items}
    return render(request, 'nettikirppis/items.html', context)

def item(request, item_id):
    item = Item.objects.get(id=item_id)
    comments = item.comment_set.order_by('date_added')
    replies = Reply.objects.filter(original_comment__in=[c.id for c in comments])
    context = {'item':item, 'comments':comments, 'replies':replies}
    return render(request, 'nettikirppis/item.html', context)

@login_required
def new_item(request):
    if request.method != 'POST':
        form = ItemForm()
    else:
        form = ItemForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item=form.save(commit=False)
            new_item.owner=request.user
            new_item.save()
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
            new_comment.owner=request.user
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

@login_required
def owner_items(request):
    items = Item.objects.filter(owner=request.user).order_by('date_added')
    context = {'items':items}
    return render(request, 'nettikirppis/owner_items.html', context)

@login_required
def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method != 'POST':
        form = ItemForm(instance=item)
    else:
        form = ItemForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('nettikirppis:items')
    
    context = {'item':item, 'form':form}
    return render(request, 'nettikirppis/edit_item.html', context)

@login_required
def delete_item(request, item_id):
    item=Item.objects.get(id=item_id)

    if request.method == "POST":
        item.delete()
        return redirect('nettikirppis:owner_items')
    
    context = {'item': item}
    return render(request, 'nettikirppis/delete_item.html', context)

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    item = comment.item

    if request.method == "POST":
        comment.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': True, 'error':'Invalid request method'})

@login_required
def new_reply(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    item = comment.item

    if request.method != 'POST':
        form = ReplyForm()
    else:
        form = ReplyForm(data=request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.owner = request.user
            new_reply.item = item
            new_reply.original_comment = comment
            form.save()
            return redirect('nettikirppis:item', item_id = item.id)
        
    context = {'item':item,'comment':comment, 'form':form}
    return render(request, 'nettikirppis/new_reply.html', context)
    