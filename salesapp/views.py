from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse
from .models import product,order,client
# def home(request):
	# ps = product.objects.all()
	# p_names = list()
	# for p in ps:
		# p_names.append(p.pname)
	# response_html = '<br>'.join(p_names)
	# return HttpResponse(response_html)
def home(request):
	ps = product.objects.all()
	return render(request, 'home.html', {'ps': ps})
def client_details(request, pk):
	p = order.objects.filter(opid=pk)
	return render(request, 'client.html', {'p': p})
def order_details(request, rk):
	k = order.objects.filter(opid=rk)
	return render(request, 'order.html', {'k': k})
# Create your views here.
