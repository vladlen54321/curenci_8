from django.urls import reverse_lazy
from currency.models import Source, ContactUs, ResponseLog
from currency.froms import SourceForm
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings


class IndexView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'currency/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Source.objects.count()
        return context


class SourceListView(generic.ListView):
    queryset = Source.objects.all()
    template_name = 'currency/rate_list.html'


class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:email_ms')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'currency/rate_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:email_ms')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:email_ms')


class SourceDetailsView(generic.DetailView):
    queryset = Source.objects.all()
    template_name = 'currency/rate_details.html'


class ContactUsCreateView(generic.CreateView):
    model = ContactUs
    success_url = reverse_lazy('currency:email_ms')
    template_name = 'currency/contactus_create.html'
    fields = (
        'email_from',
        'email_to',
        'subject',
        'message',
    )

    def form_valid(self, form):
        response = super().form_valid(form)

        subject = 'ContactUs From Currency Project'
        body = f'''
        Subject From Client: {self.object.subject}
        Email: {self.object.email_from}
        Wants to contact
        '''

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return response


class ResponseCreateView(generic.ListView):
    model = ResponseLog
    success_url = reverse_lazy('currency:email_ms')
    template_name = 'currency/response.html'
    fields = (
        'response_time',
        'request_method',
        'query_params',
        'ip',
        'path',
    )


# def index(request):
#     return render(request, 'currency/index.html')


# def email_ms(request):
#     context = {
#         # 'rate_list': ContactUs.objects.all(),
#         'source': Source.objects.all(),
#     }
#     # return HttpResponse(html_template)
#     return render(request, 'currency/rate_list.html', context=context)

# def http_response(request):
#     return HttpResponse('OK')

# def rate_update(request, rate_id):

#     try:
#         rate_instance = Source.objects.get(id=rate_id)
#     except Source.DoesNotExist:
#         raise Http404

#     rate_instance = get_object_or_404(Source, id=rate_id)

#     if request.method == 'POST':
#         form = SourceForm(request.POST, instance=rate_instance)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/email_ms/')
#     elif request.method == 'GET':
#         form = SourceForm(instance=rate_instance)

#     context = {'form': form}
#     return render(request, 'currency/rate_update.html', context=context)


# def rate_create(request):
#     if request.method == 'POST':
#         form = SourceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/email_ms/')
#     elif request.method == 'GET':
#         form = SourceForm()

#     context = {'form': form}
#     return render(request, 'currency/rate_create.html', context=context)


# # def rate_details(request, rate_id):
# #     rate_instance = get_object_or_404(ContactUs, id=rate_id)
# #     context = {'instance': rate_instance}
# #     return render(request, 'currency/rate_details.html', context=context)

# def rate_delete(request, rate_id):
#     rate_instance = get_object_or_404(Source, id=rate_id)

#     if request.method == "POST":
#         rate_instance.delete()
#         return HttpResponseRedirect('/email_ms/')

#     context = {'instance': rate_instance}
#     return render(request,'currency/rate_delete.html', context=context )

'''
GET - retriver from server
POST - send data to server


GET - read
POST - creat
PUT/PATCH - update
DELETE - delete
'''
