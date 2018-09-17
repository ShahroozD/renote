from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # API
    re_path(r'^$', views.login_handler),
    re_path(r'^dashboard$', views.dashboard_handler),
    # re_path(r'^user_login/$', views.user_login_handler),
    # re_path(r'^user_profile/$', views.user_profile_handler),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
