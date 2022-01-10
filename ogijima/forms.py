from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from .models import Contact

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

class ApplyForm(forms.Form):
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
    text = forms.CharField(
        label='本文',
        max_length=1000,
        required=True,
        widget=forms.Textarea({
            "rows": 3,
            "cols": "",
        }),
    )
    file1 = forms.fields.FileField(
        label='file1',
        required=True,
        widget=forms.widgets.FileInput,
        # validators=[FileExtensionValidator(['pdf'])]
    )
    file2 = forms.fields.FileField(
        label='file2',
        required=True,
        widget=forms.widgets.FileInput,
        # validators=[FileExtensionValidator(['pdf'])]
    )

    def send_email(self):
        # print(self)
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        text = self.cleaned_data['text']
        file1 = self.cleaned_data['file1']
        file2 = self.cleaned_data['file2']
        subject = "【男木島名物倉庫『あいきえん』】お問い合わせ内容の確認"
        message = """※このメールはシステムからの自動返信です。

{name} 様
お問い合わせいただきありがとうございます。
以下の内容で承りました。

━━━━━━□■□　お問い合わせ内容　□■□━━━━━━
お名前 ： {name}

メールアドレス ： {email}

お問い合わせ内容：
{text}
━━━━━━━━━━━━━━━━━━━━━━━━━━


担当の者より、数日で返信させていただきますので、今しばらくお待ちくださいませ。


※このメールは送信専用です。このメールにご返信いただいても、お返しすることができませんので、ご了承ください。
""".format(name=name, email=email, text=text)
        from_email = '男木島名物倉庫『あいきえん』お問い合わせ <{email}>'.format(email=settings.EMAIL_HOST_USER)
        recipient_list = ['{email}'.format(email=email)]
        bcc = ['{email}'.format(email=settings.EMAIL_HOST_USER),'ogijima.pj.hp@gmail.com']
        try:
            # send_mail(subject, message, from_email, recipient_list, bcc)
            email = EmailMessage(subject, message, from_email, recipient_list, bcc)
            email.attach_file(file1, file2)
            email.send()
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
    def return_email(self):
        return self.cleaned_data['email']

    def save(self):
        upload_file = self.cleaned_data['file1']
        upload_file.name = "name.pdf"
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
    
    # def save(self):
    #     upload_file = self.cleaned_data['application_file']
    #     upload_file.name = "name.pdf"
    #     file_name = default_storage.save(upload_file.name, upload_file)
    #     return default_storage.url(file_name)