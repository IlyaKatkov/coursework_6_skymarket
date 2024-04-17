from django.urls import reverse_lazy, reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from ads.paginators import ListPaginator
from ads.filters import AdFilter
from ads.forms import AdForm
from ads.permissions import IsOwner, IsAdmin, IsSelfUser


class AdViewSet(viewsets.ModelViewSet):
    """ Контроллер для объявлений """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    perms_methods = {
        'list': [],
        'retrieve': [IsAuthenticated, IsSelfUser | IsOwner | IsAdmin],
        'create': [IsAuthenticated, IsAdmin | IsSelfUser],
        'update': [IsAuthenticated, IsOwner | IsAdmin],
        'partial_update': [IsAuthenticated | IsAdmin],
        'destroy': [IsAuthenticated, IsOwner | IsAdmin],
    }
    pagination_class = ListPaginator
    paginate_by = Ad.objects.all().count
    extra_context = {
        'title': 'Sky Market',
        'object_list': Ad.objects.all()[:4]
    }

    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем наш фильтр

    def get_permissions(self):
        self.permission_classes = self.perms_methods.get(self.action, self.permission_classes)
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.author = self.request.user
        new_habit.save()


class AdListAPIView(generics.ListAPIView):
    """ Список всех объявлений """
    queryset = Ad.objects.all()
    template_name = 'ads/ad_list.html'
    serializer_class = AdSerializer
    #permission_classes = [IsAuthenticated]
    pagination_class = ListPaginator

    extra_context = {
        'title': 'Sky Market',
        'object_list': Ad.objects.all()[:4]
    }
    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем наш фильтр
    success_url = reverse_lazy('ads:ad_list')


class AdCreateAPIView(generics.CreateAPIView):
    """ Создание объявления """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsSelfUser],
    form_class = AdForm
    permission_required = 'ads.add_ad'
    success_url = reverse_lazy('ads:ad_list')

    def get_success_url(self):
        return reverse('ads:ad_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.author = self.request.user
        new_habit.save()


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр объявления """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsSelfUser | IsOwner | IsAdmin]


class AdUpdateAPIView(generics.UpdateAPIView):
    """ Изменение объявления """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin],


class AdDestroyAPIView(generics.DestroyAPIView):
    """ Удаление объявления """
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin],


class CommentViewSet(viewsets.ModelViewSet):
    """ Контроллер для отзывов """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    perms_methods = {
        'list': [],
        'retrieve': [IsAuthenticated, IsSelfUser | IsOwner | IsAdmin],
        'create': [IsAuthenticated, IsAdmin | IsSelfUser],
        'update': [IsAuthenticated, IsOwner | IsAdmin],
        'partial_update': [IsAuthenticated | IsAdmin],
        'destroy': [IsAuthenticated, IsOwner | IsAdmin],
    }

    def get_permissions(self):
        self.permission_classes = self.perms_methods.get(self.action, self.permission_classes)
        return [permission() for permission in self.permission_classes]

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.author = self.request.user
        new_habit.save()

