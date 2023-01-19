from django.contrib import admin
from .models import Place, Booking, Payment, Rate, PlaceWork, TimeWork, AuthUser
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TranslationAdmin

class PlaceWorkInline(admin.TabularInline):
    model = PlaceWork
    extra = 3
class TimeWorkInline(admin.TabularInline):
    model = TimeWork
    extra = 3
class RateInline(admin.StackedInline):
    model = Rate
    extra = 2
class PlaceAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Местоположение', {'fields': ['address','metro']}),
        ('Описание', {'fields': ['photo','description','price']}),
    ]
    inlines = [PlaceWorkInline,RateInline]
    list_display = ('title', 'metro')
    list_filter = ('metro', 'price')
    class Meta:
        proxy = True

class RateAdmin(ImportExportModelAdmin, SimpleHistoryAdmin,admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Описание', {'fields': ['type','photo','description','capacity']}),
        ('Тарифы', {'fields': ['price_hour','price_week','price_month']}),
    ]
    list_display = ('title', 'place','photo')
    list_filter = ('place', 'type')
    class Meta:
        proxy = True

class BookingAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('rate', 'start_time', 'time_over')
    class Meta:
        proxy = True

class PaymentAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('receipt_number', 'user', 'booking')
    class Meta:
        proxy = True

class TimeWorkAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ('week_day', 'start_time', 'end_time')
    class Meta:
        proxy = True
    
@admin.register(AuthUser)
class AuthUsers(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

admin.site.register(Place, PlaceAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(TimeWork, TimeWorkAdmin)
# Register your models here.
