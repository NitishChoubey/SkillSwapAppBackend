from rest_framework import serializers
from .models import User , ProfileDetails


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id' , 'email' , 'first_name' , 'last_name' , 'phone']

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProfileDetails
    fields = ['dob' , 'occupation' , 'skill' , 'experience' , 'location' , 'workLink' , 'description' , 'achievements']
