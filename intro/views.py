from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results
    })
    
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})
    
#   Replaced by django form in side if statement     
 #       new_item = Item()
  #      new_item.name = request.POST.get('name')
   #     new_item.done = 'done' in request.POST
    #    new_item.save()
    #    
     #   return redirect(get_todo_list)
     
def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})
        
def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)
    
    
    
    
    
    