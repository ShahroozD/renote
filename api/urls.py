from django.urls import re_path
from . import views

urlpatterns = [

    # API
    re_path(r'^user_signup/$', views.user_signup_handler),
    re_path(r'^sms_verifi/$', views.sms_verification_handler),
    re_path(r'^user_login/$', views.user_login_handler),
    re_path(r'^user_profile/$', views.user_profile_handler),
    re_path(r'^submit_post/$', views.submit_post_handler),

    re_path(r'^user_posts_list/$', views.user_posts_list_handler),

    re_path(r'^post_details/$', views.post_details_handler),
    re_path(r'^like_post/$', views.like_post_handler),
    re_path(r'^following/$', views.following_handler),

    re_path(r'^users_page/$', views.users_page_handler),
    re_path(r'^explore_posts_list/$', views.explore_posts_list_handler),
    #
    # url(r'^week_analysis/$', views.week_analysis_handler, name='week_analysis_handler'),
    # url(r'^best_week_analysis/$', views.best_week_analysis_handler, name='best_week_analysis_handler'),
    #
    #
    #
    re_path(r'^user_logout/$', views.user_logout_handler),
    #
    #
    # url(r'^defaults_val/$', views.defaults_val_handler, name='defaults_val_handler'),
    # url(r'^is_on/$', views.is_on_handler, name='is_on_handler'),

]
