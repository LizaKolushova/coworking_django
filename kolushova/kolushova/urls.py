"""kolushova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from booking.views import UserViewSet, PlaceViewSet, RateViewSet, BookingViewSet, PaymentViewSet, GetRateView, GetBookingView, GetPaymentView, GetUserView ,PostDelGetPlace

def trigger_error(request):
    division_by_zero = 1 / 0

router = DefaultRouter()
router.register('place', PlaceViewSet)
router.register('rate', RateViewSet)
router.register('booking', BookingViewSet)
router.register('payment', PaymentViewSet)
router.register('user', UserViewSet)

# from booking.models import AuthUser
# from rest_framework import routers, serializers, viewsets

# # Сериализаторы описывают представление данных.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = AuthUser
#         fields = ['url', 'username', 'email', 'is_staff']

# # Наборы представлений описывают поведение представлений.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = AuthUser.objects.all()
#     serializer_class = UserSerializer

# # Роутеры позволяют быстро и просто сконфигурировать адреса.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include('booking.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls), # admin site
    # path(r'api/', include(router.urls)),
    # path(r'api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api/', include(router.urls)),
    path('api/user-filter/', GetUserView.as_view()),
    path('api/rate-filter/', GetRateView.as_view()),
    path('api/booking-filter/', GetBookingView.as_view()),
    path('api/payment-filter/', GetPaymentView.as_view()),
    path('sentry-debug/', trigger_error),
]
