from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}

class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    username = None
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    phone = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(unique=True, verbose_name='Email')
    image = models.ImageField(upload_to='users', **NULLABLE, verbose_name='аватар')
    role = models.CharField(max_length=100, default=UserRoles.USER, choices=UserRoles.choices, verbose_name='Роль')
    is_active = models.BooleanField(default=False, verbose_name='Активность пользователя')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

