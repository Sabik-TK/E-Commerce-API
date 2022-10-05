from .models import Product
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission

# Create your views here.
class IsAdminOrReadOnly(BasePermission):
    
    """
    Only admin can add or update new instance
    Authenticated members can only   view these instance 
    """
    def has_permission(self, request, view):
        if not request.user.is_anonymous and request.user.is_admin:
            return True
        elif request.user.is_authenticated and view.action == 'list' :
            return True
        else:
            return False

class ProductViewSet(ModelViewSet):

    permission_classes = [IsAdminOrReadOnly]
    queryset         = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
 