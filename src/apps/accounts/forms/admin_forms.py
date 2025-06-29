from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from ..models import User
from .base_forms import BaseUserCreationForm


# 管理画面用ユーザー新規作成フォーム
class CustomUserCreationForm(BaseUserCreationForm):
    pass


# 管理画面用ユーザーデータ更新フォーム
class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="パスワード（ハッシュ化済）")


    class Meta:
        model = User
        fields = [
            'email',
            'last_name',
            'first_name',
            'password',
            'is_active',
            'is_staff',
            'is_superuser'
        ]