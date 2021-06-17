from djangoTest.forms import orderForm
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = orderForm()
        return render(request,'index.html',{'form':form})        