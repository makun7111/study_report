from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from ..models import Diary
class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""
    def setUp(self):
        """テストメソッド実行前の事前設定"""
    # テストユーザーのパスワード #
        self.password = 'Maumau1010'
    #23 各インスタンスメソッドで使うテスト用ユーザーを生成し # インスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
        username='makun1010it@gmail.com',
        email='makun1010it@gmail.com',
        password=self.password)
# テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)
class TestDiaryCreateView(LoggedInTestCase):
    """ DiaryCreateView用のテストクラス"""
    def test_create_diary_success(self):
        """日記作成処理が成功することを検証する"""
        params = {'title': 'テストタイトル',
                    'content': '本文',
                    'photo1': '',
                    'photo2': '',
                    'photo3':''}

        response=self.client.post(reverse_lazy('diary:diary_create'),params)

        self.assertEqual(Diary.objects.filter(title='テストタイトル').count(), 1)

    def test_create_diary_failure(self):
            """新規日記作成処理が失敗することを検証する"""
            # 新規日記作成処理 (Post)を実行
            response = self.client.post(reverse_lazy('diary:diary_create'))
            # 必須フォームフィールドが未入力によりエラーになることを検証
            self.assertFormError(response, 'form','title', 'このフィールドは必須です。')

class TestDiaryUpdateView(LoggedInTestCase):
    """DiaryUpdateView用のテストクラス"""
    def test_update_diary_success(self):
        """日記編集処理が成功することを検証する"""
        diary=Diary.objects.create(user=self.test_user,title='タイトル編集前')
        params = {'title':'タイトル編集後'}

        response=self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk':diary.pk}), params)
        self.assertRedirects(response,reverse_lazy('diary:diary_detail', kwargs={'pk':diary.pk}))
        self.assertEqual(Diary.objects.get(pk=diary.pk).title,'タイトル編集後')

    def test_update_diary_failure(self):

        """日記編集処理が失敗することを検証する"""

                        # 23 日記編集処理(Post)を実行
        response = self.client.post(reverse_lazy('diary:diary_update', kwargs = {'pk':999} ))
                        # 存在しない日記データを編集しようとしてエラーになることを検証 self.assertEqual(response.status_code, 404)

class TestDiaryDeleteView(LoggedInTestCase):
    """DiaryDeleteView用のテストクラス"""
    def test_delete_diary_success(self):
        """日記削除処理が成功することを検証する"""
        diary=Diary.objects.create(user=self.test_user,title='タイトル')
        response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk':diary.pk}))
        self.assertRedirects(response,reverse_lazy('diary:diary_list'))
        self.assertEqual(Diary.objects.filter(pk=diary.pk).count(),0)
    def test_delete_diary_failure(self):
        """日記削除処理が失敗することを検証する"""
        response=self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk': 999}))
        self.assertEqual(response.status_code,404)


