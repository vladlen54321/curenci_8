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


'''
GET - retriver from server
POST - send data to server


GET - read
POST - creat
PUT/PATCH - update
DELETE - delete
'''
