from rest_framework import serializers 
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=255)
    phone = PhoneNumberField(allow_null=False, allow_blank=False)
    
    password2 = serializers.CharField(label='Confirm Password', style={'input_type':'password'}, min_length=8, write_only=True)
    
    class Meta:
        model = User
        ref_name="Users"
        fields= [
        'username',
        'email',
        'phone',
        'password',
        'password2'
        ]
        extra_kwargs = {
            'password':
                {'write_only':True,
                 'style':{
                     'input_type':'password'
                     }
                 }
        }
        
    def validate(self, attrs):
        password =attrs['password']
        password2 = attrs['password2']
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail='Username already exists')
        email_exists=User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail='Email already exists')
        phonenumber_exists = User.objects.filter(phone=attrs['phone']).exists()
        if phonenumber_exists:
            raise serializers.ValidationError(detail='Phone number has already been registered')
        if password and password2 and password != password2:
            raise serializers.ValidationError(detail='Passwords do not match')
        return super().validate(attrs)
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        phone = validated_data['phone']
        password = validated_data['password']
        return User.objects.create_user(username=username, email=email, phone=phone, password=password)
    
    
class EmailVerificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["username", "email", "phone"]
