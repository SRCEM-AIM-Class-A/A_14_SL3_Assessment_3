from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def document_list_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('documents:list')
    else:
        form = ItemForm()
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'document_list.html', {'items': items, 'form': form})

def delete_item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('documents:list')
