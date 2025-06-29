from django import forms
from .models import Contact

class CreateInquiryForm(forms.ModelForm):
    tell1 = forms.CharField(
        label="電話番号（例：090 または 03）",
        max_length=4,
        error_messages={
            'required': '電話番号の最初の部分を入力してください。',
        },
    )
    tell2 = forms.CharField(
        label="電話番号（例：1234）",
        max_length=4,
        error_messages={
            'required': '電話番号の中央の部分を入力してください。',
        },
    )
    tell3 = forms.CharField(
        label="電話番号（例：5678）",
        max_length=4,
        error_messages={
            'required': '電話番号の最後の部分を入力してください。',
        },
    )


    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'address',
            'building',
            'category',
            'detail'
        ]
        labels = {
            'first_name': '名',
            'last_name': '姓',
            'gender': '性別',
            'email': 'メールアドレス',
            'address': '住所',
            'building': '建物名',
            'category': 'お問い合わせの種類',
            'detail': 'お問い合わせ内容',
        }
        error_messages = {
            'first_name': {
                'required': '名を入力してください。',
            },
            'last_name': {
                'required': '姓を入力してください。',
            },
            'email': {
                'required': 'メールアドレスを入力してください。',
                'invalid': '正しいメールアドレスの形式で入力してください。',
            },
            'address': {
                'required': '住所を入力してください。',
            },
            'category': {
                'required': 'お問い合わせの種類を選択してください。',
            },
            'detail': {
                'required': 'お問い合わせ内容を入力してください。',
            },
        }


    def clean_tell1(self):
        data = self.cleaned_data.get('tell1')
        if not data.isdigit():
            raise forms.ValidationError('数字のみで入力してください。')
        return data


    def clean_tell2(self):
        data = self.cleaned_data.get('tell2')
        if not data.isdigit():
            raise forms.ValidationError('数字のみで入力してください。')
        return data


    def clean_tell3(self):
        data = self.cleaned_data.get('tell3')
        if not data.isdigit():
            raise forms.ValidationError('数字のみで入力してください。')
        return data


    def clean(self):
        cleaned_data = super().clean()
        tell1 = cleaned_data.get('tell1')
        tell2 = cleaned_data.get('tell2')
        tell3 = cleaned_data.get('tell3')
        if tell1 and tell2 and tell3:
            cleaned_data['tell'] = f'{tell1}-{tell2}-{tell3}'
        return cleaned_data