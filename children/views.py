from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Child
from .forms import ChildForm

# List all children for the logged-in parent
@login_required
def child_list(request):
    children = Child.objects.filter(parent=request.user)  # Only show the parent's children
    return render(request, 'children/child_list.html', {'children': children})

# View details of a specific child
@login_required
def child_detail(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    return render(request, 'children/child_detail.html', {'child': child})

# Add a new child profile
@login_required
def child_create(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.parent = request.user  # Set parent automatically
            child.save()
            return redirect('child-list')  # Redirect to the child list
    else:
        form = ChildForm()
    return render(request, 'children/child_form.html', {'form': form})

# Edit an existing child profile
@login_required
def child_update(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('child-detail', child_id=child.id)
    else:
        form = ChildForm(instance=child)
    return render(request, 'children/child_form.html', {'form': form})

# Delete a child profile
@login_required
def child_delete(request, child_id):
    child = get_object_or_404(Child, id=child_id, parent=request.user)
    if request.method == 'POST':
        child.delete()
        return redirect('child-list')
    return render(request, 'children/child_confirm_delete.html', {'child': child})
