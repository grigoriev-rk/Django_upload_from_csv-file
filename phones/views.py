from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'name':
        sorted_phones = Phone.objects.all().order_by('name')
    elif sort_by == 'min_price':
        sorted_phones = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        sorted_phones = Phone.objects.all().order_by('-price')
    else:
        sorted_phones = Phone.objects.all()
    context = {
        'phone': sorted_phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    show_phone = Phone.objects.filter(slug=slug)
    context = {"phone": show_phone}
    return render(request, template, context)
