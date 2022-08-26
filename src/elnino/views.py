from django.shortcuts import render
from .models import Product, ProductDetails

# Create your views here.


def homeView(request):
	products = Product.objects.all()
	# details = ProductDetails.objects.all()
	shirts = ProductDetails.objects.filter(product__productType='shirt')
	shorts = ProductDetails.objects.filter(product__productType='short')
	sweaters = ProductDetails.objects.filter(product__productType='sweater')


	context = {'products':products, 'shirts':shirts, 'shorts':shorts, 'sweaters':sweaters}

	return render(request, 'index.html', context)


def itemView(request, pk):
	details = ProductDetails.objects.get(id = pk)

	context = {'details':details}

	return render(request, 'item.html', context)

# def itemsView(request, pk):
# 	details = ProductDetails.objects.get(id = pk)

# 	context = {'details':details}

# 	return render(request, 'items.html', context)		

def aboutView(request):
	return render(request, 'about.html')	