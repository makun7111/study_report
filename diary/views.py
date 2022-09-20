from django.shortcuts import render
import logging
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from.forms import InquiryForm
from django.contrib import messages
from .forms import InquiryForm,DiaryCreateForm
from django.shortcuts import get_object_or_404
from django.db.models import Sum

class OnlyYouMixin(UserPassesTestMixin):
    raise_exeption=True
    def test_func(self):
        diary=get_object_or_404(Diary,pk=self.kwargs['pk'])
        return self.request.user==diary.user

class IndexView(generic.TemplateView):
    template_name="index.html"
    def sum(self,request):
        topics = Diary.objects.all().aggregate(Sum("time"))
        return render(request, "index.html", topics)

logger=logging.getLogger(__name__)
class InquiryView(generic.FormView):
    template_name="inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')
    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin,generic.ListView):
    model=Diary
    template_name='diary_list.html'
    paginate_by=2

    def get_queryset(self):
        diaries=Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries

class DiaryDetailView(LoginRequiredMixin,generic.DetailView,OnlyYouMixin):
    model=Diary
    template_name='diary_detail.html'

class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました')
        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(self.request, "日記の作成に失敗しました")
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin, generic.UpdateView,OnlyYouMixin):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm
    def get_success_url(self):
        return reverse_lazy('diary:diary_detail', kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin,generic.DeleteView,OnlyYouMixin):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request,*args,**kwargs)





