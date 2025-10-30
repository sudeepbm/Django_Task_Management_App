from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render

from base.forms import SupportForm
from base.models import HistoryModel, TaskModel

# Create your views here.
def home(request):

    if 'q' in request.GET:
        q=request.GET['q']
        tasks = TaskModel.objects.filter(Q(title_data__icontains=q) & Q(host=request.user) & Q(completed=False) | Q(desc_data__icontains=q) & Q(host=request.user) & Q(completed=False))
    else:
        tasks = TaskModel.objects.filter(host=request.user, completed=False)

    return render(request, 'home.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        title_data = request.POST['title_attr']
        desc_data = request.POST['desc_attr']
        TaskModel.objects.create(title_data=title_data, desc_data=desc_data, host=request.user)
        return redirect('home')
    return render(request, 'add.html')

def update(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        title_data = request.POST['title_attr']
        desc_data = request.POST['desc_attr']
        task.title_data = title_data
        task.desc_data = desc_data
        task.save()
        return redirect('home')
    return render(request, 'update.html', {'task': task})

def delete(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        HistoryModel.objects.create(
            title_data=task.title_data,
            desc_data=task.desc_data,
            host=task.host,
            original_id=task.id
        )
        task.delete()
        return redirect('home')
    return render(request, 'delete.html', {'task': task})

def history(request):
    tasks = HistoryModel.objects.filter(host=request.user)
    return render(request, 'history.html', {'tasks': tasks})

def completed(request):
    tasks = TaskModel.objects.filter(host=request.user, completed=True)
    return render(request, 'completed.html', {'tasks': tasks})

def mark_complete(request, pk):
    task = TaskModel.objects.get(id=pk, host=request.user)
    task.completed = True
    task.save()
    return redirect('home')

def mark_incomplete(request, pk):
    task = TaskModel.objects.get(id=pk, host=request.user)
    task.completed = False
    task.save()
    return redirect('completed')

def delete_all_history(request):
    if request.method == 'POST':
        HistoryModel.objects.filter(host=request.user).delete()
        return redirect('history')
    return redirect('history')

def restore_all_tasks(request):
    if request.method == 'POST':
        histories = HistoryModel.objects.filter(host=request.user)
        for history in histories:
            TaskModel.objects.create(
                id=history.original_id,
                title_data=history.title_data,
                desc_data=history.desc_data,
                host=history.host
            )
        histories.delete()
        return redirect('history')
    return redirect('history')

def delete_history(request, pk):
    history = HistoryModel.objects.get(id=pk, host=request.user)
    history.delete()
    return redirect('history')

def restore_task(request, pk):
    history = HistoryModel.objects.get(id=pk, host=request.user)
    TaskModel.objects.create(
        id=history.original_id,
        title_data=history.title_data,
        desc_data=history.desc_data,
        host=history.host
    )
    history.delete()
    return redirect('history')

def about(request):
    return render(request, 'about.html')

def support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            messages.success(
                request,
                "Thanks for reaching out! We'll review your request and get back to you soon.",
            )

            return redirect('support')
    else:
        # Pre-populate form with user data if logged in
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
                'email': request.user.email,
            }
        form = SupportForm(initial=initial_data)

    return render(request, 'support.html', {'form': form})