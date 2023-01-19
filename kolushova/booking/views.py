from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import Place, Booking, Payment, Rate, PlaceWork, TimeWork, AuthUser
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, PlaceSerializer, RateSerializer, BookingSerializer, PaymentSerializer
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q
from django.utils import translation
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

class PlacePagination(PageNumberPagination):
    page_size = 10
    page_sizer_query_param = 'paginate_by'
    max_page_size = 20


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    pagination_class = PlacePagination
    http_method_names = ('get', 'post', 'patch', 'delete')
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title', 'metro']
    ordering_fields = ['price']
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delPlace(self,request, pk=None):
        movie=self.queryset.get(id=pk)
        movie.delete()
        return Response('Коворкинг был удален')
    @action(methods=['Post'], detail=False, url_path='post') 
    def posPlace(self,request, pk=None):
        title=self.queryset.create(name=request.data.get('title'))
        title.save()
        return Response('Коворкинг был создан')
    @action(methods=['GET'], detail=False,
            url_path='placeget')
    def get_data(self, request, **kwargs):
        data = dict()
        data['info'] = 'тут можно вернуть'
        return Response(data)

class UserViewSet(ModelViewSet):
    queryset = AuthUser.objects.filter(Q(date_joined__year=2022)&Q(is_staff=1))
    # AuthUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['is_superuser', 'is_staff', 'is_active']

class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-capacity')
    serializer_class = RateSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['title', 'type']
    ordering_fields = ['capacity ']


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['receipt_number']

class GetRateView(ListAPIView):
    queryset = Rate.objects.all().order_by('-capacity')
    serializer_class = RateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title']
    

class GetBookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['rate']

class GetPaymentView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['receipt_number']

class PostDelGetPlace(ModelViewSet):
    queryset =Place.objects.all()
    serializer_class = PlaceSerializer
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def delPlace(self,request, pk=None):
        movie=self.queryset.get(id=pk)
        movie.delete()
        return Response('Коворкинг был удален')
    @action(methods=['Post'], detail=False, url_path='post') 
    def posPlace(self,request, pk=None):
        title=self.queryset.create(name=request.data.get('title'))
        title.save()
        return Response('Коворкинг был создан')
    @action(methods=['GET'], detail=False,
            url_path='placeget')
    def place(self, request):
        place = request.place
        data = PlaceSerializer(place).data
        return Response(data)

class GetUserView(ListAPIView):
    queryset = AuthUser.objects.filter(Q(date_joined__year=2022)|Q(is_staff=1))
    serializer_class = AuthUser


def index(request):
    return render(request,'index.html')

def places(request):
    places_list = Place.objects.order_by('title')
    # timework_list = PlaceWork.objects.prefetch_related(place = Place.id).all()
    placework_list = PlaceWork.objects.all
    timework_list = TimeWork.objects.all
    return render(request,'place/coworking.html', {'places_list':places_list,'placework_list':placework_list,'timework_list':timework_list})

def rate(request, place_id):
    try:
        a=Place.objects.get(id = place_id)
    except:
        raise Http404("Коворкинг не найден")
    rates_list = Rate.objects.order_by('type')
    return render(request,'rate/rate.html',{'place':a,'rates_list':rates_list})

def about(request):
    return render(request,'about_us/about_us.html')

def auth(request):
    return render(request,'login/auth.html')

def registration(request):
    return render(request,'login/registration.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
