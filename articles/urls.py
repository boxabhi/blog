from django.urls import path, include
from articles.views import (ListBlog, users,get_blog,
create_user,LoginView,ListComment,comment,add_comment, incrementLike)
urlpatterns = [
    path('', ListBlog.as_view() , name='home'),
    path('blog/<id>', get_blog, name='get-blog'),
    path('users' , users , name='users'),
    path('create-user',create_user,name="create-user"),
    path('comment/<blog_id>', ListComment.as_view(), name='ListComment' ),
    path('getcomment/<blog_id>', comment, name='GetComment'),
    path('postcomment',add_comment, name='PostComment'),
    path('incrementlike/<blog_id>',incrementLike, name="IncrementLike")
    
    
]


