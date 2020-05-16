import re
from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
    UserManager)

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(verbose_name='Nome de Usúario', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'O nome de usúario só pode conter letras, digitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')])
    email = models.EmailField(verbose_name='E-mail', unique=True)
    name = models.CharField(verbose_name='Nome', max_length=100, blank=True)
    is_active = models.BooleanField(verbose_name='Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField(verbose_name='É da equipe?', blank=True, default=False)
    date_joined = models.DateField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usúario'
        verbose_name_plural = 'Usúarios'


class PasswordReset(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usúario', on_delete=models.CASCADE,
            related_name='resets'
        )
    key = models.CharField('Chave', max_length=100, unique=True) 
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.created_at)
    
    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']