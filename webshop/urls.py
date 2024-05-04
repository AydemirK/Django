from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import HelloView, MainView , FunView, PostListView, PostDetailView, PostCreateView, PostUpdateView, AddReviewView
from user.views import RegisterView, LoginView, LogoutView, ProfileView

 
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("__debug__/", include("debug_toolbar.urls")),
    
    path('', MainView.as_view(), name='main_view'),
    path('hello/', HelloView.as_view(), name='hello_view'),
    path('fun/', FunView.as_view(), name='fun_view'),
    path('posts/', PostListView.as_view(), name='post_list_view'),
    path('posts/<int:post_id>/edit/', PostUpdateView.as_view(), name='post_update_view'),
    path('posts/create/', PostCreateView.as_view(), name='post_create_view'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post_detail_view'),
    path('posts/<int:post_id>/add_review/', AddReviewView.as_view(), name='add_review'),
    
    path("register/", RegisterView.as_view(), name='register_view'),
    path("login/", LoginView.as_view(), name='login_view'),
    path("logout/", LogoutView.as_view(), name='logout_view'),
    path("profile/", ProfileView.as_view(), name='profile_view')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
