from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from rest_framework.filters import SearchFilter
from .pagination import MyPagination

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset=Note.objects.all()

    serializer_class = NoteSerializer

    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        queryset=Note.objects.filter(
            user=self.request.user,
        )   
        completed=self.request.query_params.get('completed')
        if completed:
            queryset=queryset.filter(
                completed=completed.lower()=='true'
            )
        return queryset

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

permission_classes=[IsAuthenticated,IsOwner]
filter_backends=[SearchFilter]
search_fields=["content",'title']  
pagination_class = MyPagination
