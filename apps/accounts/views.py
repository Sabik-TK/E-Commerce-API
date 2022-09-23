from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from . import verify
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,BasePermission

# Create your views here.
class IsCreationOrIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True


class UserViewSet(viewsets.ModelViewSet):
    
    queryset           = Account.objects.all().order_by('id')
    serializer_class   = AccountSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def send_otp(self,request):
        phone = '+91' + request.data['phone']
        print(phone)
        verify.send(phone)
        return Response({'Message': f'OTP sent successfully to {phone}'})


    @action(detail=False, methods=['post'])
    def verify_otp(self,request):
        otp = request.data['otp']
        phone = '+91' + request.data['phone']
        if verify.check(phone,otp):
            user = Account.objects.filter(mobile=request.data['phone']).first()
            user.is_active = True
            user.save()
            return Response({'Message': 'Verified'
            })

        return Response({'Message': 'Not Verified'})

        

        