from rest_framework import serializers
from articles.models import Blog ,Comment,Category
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
   
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'     
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']
        
        
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
            user = super().create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user
        
    class Meta: 
        model = User
        fields = ['username','password']
        
        