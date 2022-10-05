from rest_framework import viewsets
from .models import Account
from .serializers import AccountSerializer
from . import verify
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission
from rest_framework import status

# Create your views here.
class IsCreationOrIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        allowed_actions = ('create','verify_otp','send_otp')
        admin_actions   = ('block_user','unblock_user')

        if not request.user.is_anonymous:
            if request.user.is_admin:
                return True
            elif request.user.is_active and not view.action in admin_actions:
                return True
        elif view.action in allowed_actions:
            return True
        else :
            return False
    
class UserViewSet(viewsets.ModelViewSet):

    queryset           = Account.objects.all().order_by('id')
    serializer_class   = AccountSerializer
    permission_classes = [IsCreationOrIsAuthenticated]

    def get_queryset(self):
        """
        Only admin can access other users
        """
        if self.request.user.is_admin:
            return Account.objects.all()
        return Account.objects.filter(pk=self.request.user.pk)

    @action(detail=False, methods=['get'])
    def send_otp(self,request):
        phone = str(request.user.mobile)
        verify.send(phone)
        return Response({'Message': f'OTP sent successfully to {phone}'}, status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'])
    def verify_otp(self,request):
        otp = request.data['otp']
        phone = str(request.user.mobile)
        if verify.check(phone,otp):
            user = request.user
            user.is_verified = True
            user.save()
            return Response({'Message': 'Verified'}, status=status.HTTP_200_OK)
            
        return Response({'Message': 'Not Verified'}, status=status.HTTP_501_NOT_IMPLEMENTED)


    @action(detail=True, methods=['get'])
    def block_user(self, request, pk=None):
        user = Account.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response(
            {'user': user.username, 'is_active': user.is_active},
            status=status.HTTP_200_OK
            )

    @action(detail=True, methods=['get'])
    def unblock_user(self,request, pk=None):
        user = Account.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return Response(
            {'user': user.username, 'is_active': user.is_active},
            status=status.HTTP_200_OK
            )

        