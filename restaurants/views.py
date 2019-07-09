from django.shortcuts import render

# Create your views here.
context = {
	"msg" : "Hello World"
}
def template(request):
	return render(request, "templates.html")

