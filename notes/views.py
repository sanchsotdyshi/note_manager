from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from .models import Note
from django.views import generic
from django.urls import reverse

# Create your views here.

class IndexView(generic.ListView):
	template_name = 'notes/index.html'
	context_object_name = 'notes_list'

	def get_queryset(self):
		return Note.objects.all()


def editor(request, notes_id=None):
	template = loader.get_template('notes/editor.html')
	if notes_id:
		note = get_object_or_404(Note, pk=notes_id)
		context = {
		'note': note
		}
		return HttpResponse(template.render(context, request))
	else:	
		return HttpResponse(template.render({}, request))

def save(request, notes_id=None):
	if notes_id:
		note = Note.objects.get(pk=notes_id)
		header = request.POST['header']
		content = request.POST['content']
		note.header = header
		note.content = content
		note.save()
		return HttpResponseRedirect(reverse('notes:edit', args=(note.id,)))
	else:
		header = request.POST['header']
		content = request.POST['content']
		note = Note(header=header, content=content)
		note.save()
		return HttpResponseRedirect(reverse('notes:edit', args=(note.id,)))