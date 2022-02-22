from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=100,
        required=True,
    )
    email = forms.EmailField(
        label='メールアドレス',
        max_length=100,
        required=True,
        widget=forms.EmailInput({
            "placeholder": "example@example.com",
        }),
    )
    title = forms.CharField(
        label='件名',
        max_length=200,
        required=True,
    )
    text = forms.CharField(
        label='本文',
        max_length=1000,
        required=True,
        widget=forms.Textarea({
            "rows": 3,
            "cols": "",
        }),
    )

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        text = self.cleaned_data['text']
        subject = "【男木島名物倉庫『あいきえん』】お問い合わせ内容の確認"
        message = """※このメールはシステムからの自動返信です。

{name} 様
お問い合わせいただきありがとうございます。
以下の内容で承りました。

━━━━━━□■□　お問い合わせ内容　□■□━━━━━━
お名前 ： {name}

メールアドレス ： {email}

件名 ： {title}

お問い合わせ内容：
{text}
━━━━━━━━━━━━━━━━━━━━━━━━━━


担当の者より、数日で返信させていただきますので、今しばらくお待ちくださいませ。


※このメールは送信専用です。このメールにご返信いただいても、お返しすることができませんので、ご了承ください。
""".format(name=name, email=email, title=title, text=text)
        from_email = '男木島名物倉庫『あいきえん』お問い合わせ <{email}>'.format(email=settings.EMAIL_HOST_USER)
        recipient_list = ['{email}'.format(email=email)]
        bcc = ['{email}'.format(email=settings.EMAIL_HOST_USER),'ogijima.pj.hp@gmail.com']
        try:
            # send_mail(subject, message, from_email, recipient_list, bcc)
            email = EmailMessage(subject, message, from_email, recipient_list, bcc)
            email.send()
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
    def return_email(self):
        return self.cleaned_data['email']

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application_contact
        fields = '__all__'
