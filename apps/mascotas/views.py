from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from apps.mascotas.forms import MascotaForm
from apps.mascotas.models import Mascota
from django.shortcuts import redirect
from django.views.generic import ListView,CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request, 'mascota/index.html')

"""def new_mascota(request):
    
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('/mascotas/lista/')
    else:
        form=MascotaForm()
    return render(request, 'mascota/mascota_form.html',{'form':form})

def mascota_list(request):
    mascota=Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota= Mascota.objects.get(id=id_mascota)
    if request.method== 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('lista')
    return render(request, 'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, id_mascota):
    mascota= Mascota.objects.get(id=id_mascota)
    if request.method== 'POST':
        mascota.delete()
        return redirect('lista')
    return render(request, 'mascota/mascota_delete.html',{'mascotas':mascota})"""

class MascotaList(ListView):
    model=Mascota
    template_name = 'mascota/mascota_list.html'
    ordering=['id']

class MascotaCreate(CreateView):
    model=Mascota
    form_class= MascotaForm
    template_name='mascota/mascota_form.html'
    success_url = reverse_lazy('lista')

class MascotaUpdate(UpdateView):
    model=Mascota
    form_class= MascotaForm
    template_name='mascota/mascota_form.html'
    success_url = reverse_lazy('lista')

class MascotaDelete(DeleteView):
    model=Mascota
    template_name='mascota/mascota_delete.html'
    success_url = reverse_lazy('lista')