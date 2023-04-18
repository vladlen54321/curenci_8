from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# from currency.utils import get_password
from currency.models import ContactUs, Source
from currency.froms import RateForm, SourceForm


def index(request):
    return render(request, 'currency/index.html')


def email_ms(request):
    context = {
        # 'rate_list': ContactUs.objects.all(),
        'source': Source.objects.all(),
    }
    # return HttpResponse(html_template)
    return render(request, 'currency/rate_list.html', context=context)

def http_response(request):
    return HttpResponse('OK')

def rate_update(request, rate_id):

    try:
        rate_instance = Source.objects.get(id=rate_id)
    except Source.DoesNotExist:
        raise Http404
    
    rate_instance = get_object_or_404(Source, id=rate_id)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=rate_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/email_ms/')
    elif request.method == 'GET':
        form = SourceForm(instance=rate_instance)

    context = {'form': form}
    return render(request, 'currency/rate_update.html', context=context)


def rate_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/email_ms/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {'form': form}
    return render(request, 'currency/rate_create.html', context=context)



def rate_details(request, rate_id):
    rate_instance = get_object_or_404(ContactUs, id=rate_id)
    context = {'instance': rate_instance}
    return render(request, 'currency/rate_details.html', context=context)

def rate_delete(request, rate_id):
    rate_instance = get_object_or_404(Source, id=rate_id)

    if request.method == "POST":
        rate_instance.delete()
        return HttpResponseRedirect('/email_ms/')
    
    context = {'instance': rate_instance}
    return render(request,'currency/rate_delete.html', context=context )

'''
GET - retriver from server 
POST - send data to server


GET - read
POST - creat
PUT/PATCH - update
DELETE - delete 
'''
