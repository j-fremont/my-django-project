from django.http import HttpResponse
from django.template import loader
from .models import Message

# Create your views here.

def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())

def comments(request):
	mymessages = Message.objects.all().values()
	template = loader.get_template('comments.html')
	context = {
		'mymessages': mymessages,
	}
	return HttpResponse(template.render(context, request))

def info(request):
	template = loader.get_template('info.html')
	return HttpResponse(template.render())
