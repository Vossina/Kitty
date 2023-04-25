from rest_framework import viewsets
from .models import Cat, Owner, Toy
from .serializers import CatSerializer, OwnerSerializer, ToySerializer


# Create your views here.
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.filter(is_purebred=True, deleted = None).order_by('-created')
    serializer_class = CatSerializer

    # def destroy(self, queryset, *args, **kwargs):
    #     deleted = timezone.now()
    #     return super().destroy(queryset, *args, **kwargs)


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer