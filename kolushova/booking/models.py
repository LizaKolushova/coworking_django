# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_price(value):
    if value < -1:
        raise ValidationError(
            _('%(value)s Прайс не может быть отрицательной'),
            params={'value': value})

def validate_workers(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Количество людей не может быть отрицательным'),
            params={'value': value})

def validate_receipt(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Номер счета не может быть отрицательным'),
            params={'value': value})

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
        
    history = HistoricalRecords()

    def __str__(self):
        return self.username
    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Booking(models.Model):
    rate = models.ForeignKey('Rate', models.DO_NOTHING)
    start_time = models.DateTimeField(db_column='start-time')  # Field renamed to remove unsuitable characters.
    time_over = models.DateTimeField(db_column='time-over')  # Field renamed to remove unsuitable characters.
    workers = models.IntegerField(validators=[validate_workers])
    # def __str__(self):
    #     return str(self.rate)
        
    history = HistoricalRecords()

    class Meta:
        managed = False
        db_table = 'booking'
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Payment(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    booking = models.ForeignKey(Booking, models.DO_NOTHING)
    receipt_number = models.IntegerField(db_column='receipt-number', validators=[validate_receipt] )  # Field renamed to remove unsuitable characters.
    date = models.DateTimeField()
        
    history = HistoricalRecords()

    def __str__(self):
        return str(self.receipt_number)
    class Meta:
        managed = False
        db_table = 'payment'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'


class Place(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    metro = models.CharField(max_length=100)
    price = models.IntegerField(validators=[validate_price])
    photo = models.CharField(max_length=300)
    description = models.TextField()
        
    history = HistoricalRecords()

    def __str__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'place'
        verbose_name = 'Коворкинг'
        verbose_name_plural = 'Коворкинги'


class PlaceWork(models.Model):
    place = models.ForeignKey(Place, models.DO_NOTHING)
    time = models.ForeignKey('TimeWork', models.DO_NOTHING, db_column='time_id')  # Field renamed to remove unsuitable characters.

    history = HistoricalRecords()

    class Meta:
        managed = False
        db_table = 'place-work'


class Rate(models.Model):
    place = models.ForeignKey(Place, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price_hour = models.IntegerField(db_column='price-hour')  # Field renamed to remove unsuitable characters.
    price_week = models.IntegerField(db_column='price-week')  # Field renamed to remove unsuitable characters.
    price_month = models.IntegerField(db_column='price-month')  # Field renamed to remove unsuitable characters.

    history = HistoricalRecords()

    def __str__(self):
        return self.title
    class Meta:
        managed = False
        db_table = 'rate'
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class TimeWork(models.Model):
    week_day = models.CharField(db_column='week-day', max_length=10)  # Field renamed to remove unsuitable characters.
    start_time = models.TimeField(db_column='start-time')  # Field renamed to remove unsuitable characters.
    end_time = models.TimeField(db_column='end-time')  # Field renamed to remove unsuitable characters.

    history = HistoricalRecords()

    def __str__(self):
        return self.week_day
    class Meta:
        managed = False
        db_table = 'time-work'
        verbose_name = 'Время работы'
        verbose_name_plural = 'Время работы'
