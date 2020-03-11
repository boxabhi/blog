from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from articles.models import Blog ,Category,Comment
from articles.serializer import BlogSerializer,CategorySerializer,UserSerializer,CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
def users(request):
    users = User.objects.all()
    print(users)
    serializers = UserSerializer(users)
    return Response(serializers.data)


@api_view(['POST'])
def create_user(request):
    serializers = UserSerializer(data = request.data)
    if serializers.is_valid():
        
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors)
    

@api_view(['GET'])
def get_blog(request,id):
    try:
        blog = Blog.objects.get(id = id)
        serializers = BlogSerializer(blog)
        return Response(serializers.data, status=200)
    except Blog.DoesNotExist:
        return Response({'message': 'error getting blog'})


class LoginView(APIView):
     authentication_classes = [SessionAuthentication, BasicAuthentication]
     permission_classes = [IsAuthenticated]
     def get(self, request, format=None):
         
         return Response({'message': 'Login Success'})


@api_view(['GET'])
def comment(request, blog_id):
    blog = Blog.objects.get(id = blog_id)
    comment = Comment.objects.filter(blog_id = blog.id)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)
    
    
@api_view(['POST'])
def add_comment(request):
    serializers = CommentSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message':'Comment added successfully'})
    else:
        return Response(serializers.errors, {'message':'Comment added failed'})
    

class ListComment(APIView):
    def get(self,request,blog_id):
        blog = Blog.objects.get(id = blog_id)
        comment = Comment.objects.filter(blog_id = blog.id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def post(self,request,blog_id):
        serializers = CommentSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Comment added successfully'})
        else:
            return Response(serializers.errors, {'message':'Comment added failed'})
    

class ListBlog(APIView):
    def get(self, request):
        queryset = Blog.objects.all()
        print(queryset)
        serializers = BlogSerializer(queryset, many=True)
        return Response(serializers.data, status=200)
    
    def post(self, request):
        serializers = BlogSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Post saved successfully'})
        else:
            return Response(serializers.errors, status=400)
            
    def put(self,request):
        blog = Blog.objects.get(id = request.POST['id'])
        serializers = BlogSerializer(blog ,data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Post updated successfully!'})
        else:
            return Response(serializers.errors,status=404)            
    def delete(self,request):
        try:
            blog = Blog.objects.get(id = request.POST['id'])
            blog.delete()
            return Response({'message':'Deleted!'})
        except Exception as e:
            return Response({'message':'Failed!'})
       
       
@api_view(['PUT'])
def incrementLike(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    print(blog)
    serializers = BlogSerializer(blog , data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message':'You liked a blog'})
    else :
        return Response(serializers.errors)