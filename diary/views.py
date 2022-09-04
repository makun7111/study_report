from django.shortcuts import render
import logging
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from.forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name="index.html"

logger=logging.getLogger(__name__)
class InquiryView(generic.FormView):
    template_name="inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')
    def form_valid(self,form):
        form.send_email()
        logger.info('inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)



