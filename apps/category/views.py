from .models import MainCategory,Category
from .serializers import MainCategorySerializer,CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission

# Create your views here.
class IsAdminOrReadOnly(BasePermission):
    
    """
    Only admin can add or update new instance
    Authenticated members can view these instance 
    """
    def has_permission(self, request, view):
        
        if request.user.is_anonymous:
            return False
        elif request.user.is_admin:
            return True
        elif request.user.is_authenticated and view.action == 'list' :
            return True
        else:
            return False



class MainCategoryViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    queryset           = MainCategory.objects.all().order_by('id')
    serializer_class   = MainCategorySerializer


class CategoryViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    queryset           = Category.objects.all().order_by('id')
    serializer_class   = CategorySerializer
