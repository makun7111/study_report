from accounts.models import CustomUser
from django.db import models
class Diary(models. Model):

    user = models.ForeignKey(CustomUser,verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    time = models.IntegerField(verbose_name='時間')
    materials = models.CharField(verbose_name='教材',max_length=40)
    comment = models.TextField(verbose_name='コメント',blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時',auto_now=True)

    class Meta:
        verbose_name_plural='Diary'
        def __str__(self):
            return self.title

# Create your models here.
