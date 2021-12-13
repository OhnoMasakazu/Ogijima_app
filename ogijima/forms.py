from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

class ContactForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100)
    email = forms.EmailField(label='メール', max_length=100)
    title = forms.CharField(label='件名', max_length=200)
    text = forms.CharField(label='本文', max_length=1000)

    def send_email(self):
        subject = "お問い合わせ内容の確認"
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        message = "お問い合せが完了しました．\n件名\n"+title+"\n本文"+text
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['{name} <{email}>'.format(name=name, email=email)]  # 受信者リスト
        bcc = [settings.EMAIL_HOST_USER]
        try:
            send_mail(subject, message, from_email, recipient_list, bcc)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")