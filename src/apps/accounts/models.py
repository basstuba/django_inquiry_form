from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email) # メールのドメイン部分を小文字に変換
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # パスワードをハッシュ化
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError("メールアドレスを入力してください。")

        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("有効なメールアドレスを入力してください。")

        if not password:
            raise ValueError("パスワードを入力してください。")

        if not first_name:
            raise ValueError("名を入力してください。")

        if not last_name:
            raise ValueError("姓を入力してください。")

        extra_fields['first_name'] = first_name
        extra_fields['last_name'] = last_name
        extra_fields.setdefault('is_active', True) # 権限の初期設定
        extra_fields.setdefault('is_staff', False) # 権限の初期設定
        extra_fields.setdefault('is_superuser', False) # 権限の初期設定
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, password, first_name=None, last_name=None, **extra_fields):
        if not email:
            raise ValueError("メールアドレスを入力してください。")

        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("有効なメールアドレスを入力してください。")

        if not password:
            raise ValueError("パスワードを入力してください。")

        if not first_name:
            raise ValueError("名を入力してください。")

        if not last_name:
            raise ValueError("姓を入力してください。")

        extra_fields['first_name'] = first_name
        extra_fields['last_name'] = last_name
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_("first_name"),
        max_length=100,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=_("last_name"),
        max_length=100,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        verbose_name=_("active"),
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name=_("staff"),
        default=False
    )
    is_superuser = models.BooleanField(
        verbose_name=_("superuser"),
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated_at"),
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email' # Djangoの認証はusernameがデフォルトなのでemailに変更
    REQUIRED_FIELDS = ['first_name', 'last_name'] # createsuperuserコマンド実行時にfirst_nameとlast_nameを入力必須としている

    def __str__(self):
        return f'{self.last_name} {self.first_name} <{self.email}>'