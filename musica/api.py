from rest_framework import viewsets

from .models import Musica
from .serializers import MusicaSerializer

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

# class ItemViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer

#     def get_queryset(self):
#         return Item.objects.filter(
#             channel=self.kwargs["channel_pk"])