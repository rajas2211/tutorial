from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
	#On receiving HttpResponse, this will be exectuted
	
	def __init__(self,data,**kwargs):
		
		content=JSONRenderer().render(data)
		kwargs['content_type']='application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):

	if request.method=='GET':
		snippets=Snippet.objects.all()
		serialzer=SnippetSerializer(snippets, many=True)
		return JSONResponse(serialzer.data)

	elif request.method=='POST':
		data=JSONParser()parse(request)
		serialzer=SnippetSerializer(data=data)
		if serialzer.is_valid():
			serialzer.save()
			return JSONResponse(serializer.data,status=201)
		return JSONResponse(serialzer.errors, status=400)

def snippet_detail(request,pk):
	
	try:
		snippet=Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExsist:
		return HttpResponse(status=404)

	if request.method=='GET':
		serialzer= SnippetSerializer(snippet)
		return JSONResponse(serializer.data)

	elif request.method=='PUT':
		data=JSONParser().parse(request)
		serialzer=SnippetSerializer(snippet,data=data)
		if serialzer.is_valid():
			serialzer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method=='DELETE':
		snippet.delete()
		return HttpResponse(status=204)



