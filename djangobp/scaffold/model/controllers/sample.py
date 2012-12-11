from django.http import HttpResponseRedirect
from djangobp.makohelper import render_to_response
from django.forms.models import ModelForm, ModelChoiceField
from django.forms.widgets import HiddenInput
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from djangobp.scaffold.model.models import Sample
from django.template.context import RequestContext

class SampleForm(ModelForm):
    class Meta:
        model = Sample

model_class = Sample
controller = __name__.split('.')[-1]
form_class = SampleForm

def path():
    return reverse(__name__ + '.index')
        
page_size = 20

def index(request):
    page = int(request.GET.get('page', 1))
    paginator = Paginator(model_class.objects.all(), page_size)
    current_page = paginator.page(page)
    
    return render_to_response(controller + '/index.html', locals())

def show(request, resource_id):
    item = model_class.objects.get(id=resource_id)
    return render_to_response(controller + '/show.html', locals())

def new(request):
    form = form_class(initial={'owner':request.user})
    return render_to_response(controller + '/new.html', locals(), RequestContext(request))

def create(request):
    form = form_class(request.POST)
    if form.is_valid():
        item = form.save()
        return HttpResponseRedirect(path() + '/%s' % item.id)
    else:
        return render_to_response(controller + '/new.html', locals())
    

def edit(request, resource_id):
    item = model_class.objects.get(id=resource_id)
    form = form_class(instance=item)
    return render_to_response(controller + '/edit.html', locals(), RequestContext(request))

def update(request, resource_id):
    item = model_class.objects.get(id=resource_id)
    form = form_class(request.POST, instance=item)
    
    if form.is_valid():
        item = form.save()
        return HttpResponseRedirect(path() + '/%s' % item.id)
    else:
        return render_to_response(controller + '/edit.html', locals())

def delete(request, resource_id):
    model_class.objects.filter(id=resource_id).delete()
    return HttpResponseRedirect(path())
