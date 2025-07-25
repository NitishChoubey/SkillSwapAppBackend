from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User , ProfileDetails
from .serializers import ProfileSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser , FormParser

# Create your views here.

class RegisterView(APIView):
  def post(self, request):
    data = request.data
    if User.objects.filter(email = data['email']).exists():
      return Response({'error': 'Email already exists'}, status = status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(
      email = data['email'],
      first_name = data['first_name'] , 
      last_name = data['last_name'] , 
      phone = data['phone'],
      password = data['password']
    )
    return Response({'message':'User created successfully'} , status = status.HTTP_201_CREATED)
  
class LoginView(APIView):
  def post(self , request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(email = email , password = password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh' : str(refresh) ,
        'access' : str(refresh.access_token),
      })
    else:
      return Response({'error' : 'Invalid credentials'} , status = status.HTTP_401_UNAUTHORIZED)

class ProfileUpdateView(APIView):
  # Is line ka matlab hai ki is API ko sirf logged-in user hi access kar sakta hai.
  # Agar user ka token valid nahi hoga, toh use "401 Unauthorized" error milega.
  permission_classes = [IsAuthenticated]

  

  def get(self , request , *args , **kwargs):
    # Yeh line logged-in user (request.user) ke liye 'Profile' model mein entry dhoondhti hai.
    # Agar entry mil jaati hai, toh 'profile' mein aa jaayegi.
    # Agar nahi milti, toh ek nayi entry bana degi. 'created' se pata chalta hai ki nayi bani ya nahi.

    profile , created = ProfileDetails.objects.get_or_create(user = request.user)

     # ProfileSerializer ko profile object diya jaata hai taaki woh usse JSON format mein badal sake.
    serializer = ProfileSerializer(profile)
     # Serializer dwara banaye gaye JSON data ko app ko waapis bhej diya jaata hai.

    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
        profile, created = ProfileDetails.objects.get_or_create(user=request.user)

        # Yahan serializer ko 3 cheezein di jaati hain:
        # 1. instance=profile: Isse pata chalta hai ki humein ek nayi entry nahi banani, balki is 'profile' object ko update karna hai.
        # 2. data=request.data: Yeh app se bheja gaya saara text data hai (dob, bio, etc.).
        # 3. partial=True: Iska matlab hai ki agar app saari fields na bhi bheje, toh bhi error na aaye. Sirf bheji gayi fields hi update hongi.
        serializer = ProfileSerializer(instance=profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
           
            updated_serializer = ProfileSerializer(profile)
            return Response(updated_serializer.data, status=200)
        else:
            print("Serializer Errors:", serializer.errors) 
            return Response(serializer.errors, status=400)
        

class ProfilePictureUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser] # Parser sirf yahan rahega

    def post(self, request, *args, **kwargs):
        profile, created = ProfileDetails.objects.get_or_create(user=request.user)
        
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            return Response({"message": "Image uploaded successfully!"}, status=200)
        else:
            return Response({"error": "No image file provided."}, status=400)
  

  

  

