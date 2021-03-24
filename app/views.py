from django.shortcuts import render,redirect
from app.forms import AddForm
from app.models import PostData
from django.contrib import messages
# Create your views here.

def home(request):
    '''
    This function accept 2 type of requests either it can be post or get
    GET request: it will render the page that consist of the form
    POST request: this will fetch the data and validat it. All validation are custom. After validation it saves the data in DB
    '''
    form = AddForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Data has been saved')
            return redirect('app-home')
    return render(request, 'home.html', {'form': form})