from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="メールアドレス",
        error_messages={
            'required': 'メールアドレスを入力してください。',
            'invalid': '正しいメールアドレスの形式で入力してください。',
        },
    )
    password = forms.CharField(
        label="パスワード",
        min_length=8,
        error_messages={
            'required': 'パスワードを入力してください。',
            'min_length': 'パスワードは8文字以上で入力してください。',
        },
        widget=forms.PasswordInput
    )