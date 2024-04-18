from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import main_view, hello_view, fun_view, post_list_view, post_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('hello/', hello_view),
    path('fun/', fun_view),
    path('posts/', post_list_view),
    path('posts/<int:post_id>/', post_detail_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
