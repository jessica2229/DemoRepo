from django.shortcuts import render ,redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import StudentForm
from .models import Students

# Create your views here.
class StudentCreateView(CreateView):
    model = Students
    #form_class = StudentForm
    fields = ['name','email','city']
    template_name = 'Students_form.html'
    success_url = reverse_lazy('StudentListView')
    """ def get(self,request):
        form = StudentForm()
        return render(request,"formpage.html",{'form':form})
    
    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('StudentListView')
        return render(request,"formpage.html",{'form':form}) """
    

class StudentListView(ListView):
     model = Students
     template_name = "index.html"

     """ def get(self,request):
        data = Students.objects.all()
        return render(request,"index.html",{'data':data}) """
    


class StudentUpdateView(UpdateView):
    model = Students
    fields = ['name','email','city']
    template_name = 'Students_form.html'
    success_url = reverse_lazy('StudentListView')
    """ def get(self, request, pk):
        instance = get_object_or_404(Students, pk=pk)
        form = StudentForm(instance=instance)
        return render(request, "update_form.html", {'form': form})

    def post(self, request, pk):
        instance = get_object_or_404(Students, pk=pk)
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('StudentListView')
        return render(request, "update_form.html", {'form': form}) """
    
class StudentDeleteView(DeleteView):
    model = Students
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('StudentListView')
    """ def get(self, request, pk):
        instance = get_object_or_404(Students, pk=pk)
        return render(request, "confirm_delete.html", {'instance': instance})

    def post(self, request, pk):
        instance = get_object_or_404(Students, pk=pk)
        instance.delete()
        return redirect('StudentListView')  # Assuming you have a URL named 'student_list' """