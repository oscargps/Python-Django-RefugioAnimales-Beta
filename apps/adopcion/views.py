from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import SolicitudForm, PersonaForm
# Create your views here.
def index(request):
    return HttpResponse('Adopcion')

class SolicitudList(ListView): #clase para listar solicitudes
	model=Solicitud #el modelo es el de solicitud
	template_name= 'adopcion/solicitud_list.html' #asigno el template de listar
	ordering=['id']  #el listado se ordena por id

class SolicitudCreate(CreateView): #clase para crear una nueva solicitud
	model=Solicitud #asigno el modelo
	form_class=SolicitudForm # asigno el formulario	
	second_form_class = PersonaForm #un segundo formulario
	template_name='adopcion/solicitud_form.html' #asigno el template
	success_url = reverse_lazy('Lista') #la url cuando haya un submit

	def  get_context_data(self, **kwards): #metodo que recibe varios argumentos
		context= super(SolicitudCreate, self). get_context_data(**kwards) #indico el contexto 
		if 'form' not in context: #si el formulario no esta en el contexto
			context['form'] = self.form_class(self.request.GET) 
		if 'form2' not in context:
			context['form2']= self.second_form_class(self.request.GET)
		return context
	#segun parece se crea un contexto con los dos formularios

	def post(self, request, *args, **kwargs): #metodo post de los formularios
		self.object = self.get_object #se recibe el objeto que devuelve la consulta
		form = self.form_class(request.POST) 
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid(): #si ambos formularios son validos
			solicitud = form.save(commit=False) 
			solicitud.persona = form2.save()
			solicitud.save() #guardo los formularios
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2)) 

class SolicitudUpdate(UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class= SolicitudForm
	second_form_class = PersonaForm
	success_url= reverse_lazy('Lista')

	def get_context_data(self, **kwargs):
		context = super(SolicitudUpdate, self).get_context_data(**kwargs)
		pk= self.kwargs.get('pk', 0)
		solicitud = self.model.objects.get(id=pk)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		if 'form' not in context: #si el formulario no esta en el contexto
			context['form'] = self.form_class() 
		if 'form2' not in context:
			context['form2']= self.second_form_class(instance=persona)
		context['id'] = pk
		return context
    
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_delete.html'
	success_url = reverse_lazy('Lista')