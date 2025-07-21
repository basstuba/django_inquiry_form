from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from ..models import User


class BaseUserCreationForm(forms.ModelForm):
    last_name = forms.CharField(
        label="姓",
        error_messages={
            'required': '姓を入力してください。',
        },
    )
    first_name = forms.CharField(
        label="名",
        error_messages={
            'required': '名を入力してください。',
        },
    )
    email = forms.EmailField(
        label="メールアドレス",
        error_messages={
            'required': 'メールアドレスを入力してください。',
            'invalid': '正しいメールアドレスの形式で入力してください。',
        },
    )
    password1 = forms.CharField(
        label="パスワード",
        min_length=8,
        error_messages={
            'required': 'パスワードを入力してください。',
            'min_length': 'パスワードは8文字以上にしてください。',
        },
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="確認用パスワード",
        error_messages={
            'required': 'パスワードを入力してください。',
        },
        widget=forms.PasswordInput
    )


    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("このメールアドレスはすでに登録されています。")
        return email


    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password.isdigit():
            raise forms.ValidationError("パスワードは英数字で入力してください。")


        try:
            validate_password(password)
        except DjangoValidationError:
            raise forms.ValidationError("パスワードは8文字以上の英数字で入力してください。")
        return password


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'パスワードが一致しません。')
        return cleaned_data


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user