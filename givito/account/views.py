from rest_framework import views, permissions, response, generics, status
from givito.account.models import User

from givito.account.serializers import ChangePasswordSerializer, UserSerializer

class UserRegisterView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            passwd = request.data['password']
            passwd_confirm = request.data['password_confirmation']
        except:
            return response.Response({"error": "password must be set"},status=status.HTTP_400_BAD_REQUEST)
        
        if(not passwd == passwd_confirm):
            return response.Response({"error": "password does not match"},status=status.HTTP_403_FORBIDDEN)
            
        return super().create(request, *args, **kwargs)

class UserMeView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = User
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
        
class UserMeChangePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return response.Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            resp = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return response.Response(resp)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)