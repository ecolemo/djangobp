from djangobp.makohelper import render_to_response
from django.http import HttpResponseRedirect

class GenericModelController(object):
    def __init__(self, model, name=None):
        self.model = model
        if name:
            self.name = name
        else:
            self.name = model.__name__.lower()
        
    def index(self, request):
        objects = self.model.objects.all()
        return render_to_response('/%s/index.html' % self.name, locals())
    
    def show(self, request, resource_id):
        item = self.model.objects.get(id=resource_id)
        return render_to_response('/%s/show.html' % self.name, locals())
    
    def new(self, request):
        return render_to_response('/%s/new.html' % self.name, locals())
        
    def create(self, request):
        item = self.model.objects.create()
        return HttpResponseRedirect('/%s/%s' % (self.name, item.id))
        
    def edit(self, request):
        return render_to_response('/%s/edit.html' % self.name, locals())

    def update(self, request, resource_id):
        item = self.model.objects.get(id=resource_id)
        return HttpResponseRedirect('/%s/%s' % (self.name, item.id))
        
    def delete(self, request, resource_id):
        self.model.objects.filter(id=resource_id).delete()
        return HttpResponseRedirect('/%s' % (self.name,))