
from django.conf.urls import patterns, include, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xxx.views.home', name='home'),
    # url(r'^xxx/', include('xxx.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^$', index),
    ('^index/$', index),
    ('^community/$', community),
    ('^building/$', building),
    ('^house/$', house),

    ('^zxcj/$', zxcj),
    ('^xqxxs/$', xqxxs),
    ('^bmfw/$', bmfw),
    ('^wtczcs/$', wtczcs),


    ('^admin_community/$', admin_community),
    ('^admin_community_add/$', admin_community_add),
    ('^admin_community_del/$', admin_community_del),
    ('^admin_community_update/$', admin_community_update),

    ('^admin_building/$', admin_building),
    ('^admin_building_add/$', admin_building_add),
    ('^admin_building_del/$', admin_building_del),
    ('^admin_building_update/$', admin_building_update),

    ('^admin_house/$', admin_house),
    ('^admin_house_add/$', admin_house_add),
    ('^admin_house_del/$', admin_house_del),
    ('^admin_house_update/$', admin_house_update),
    ('^admin_pic_del/$', admin_pic_del),

    ('^admin_info/$', admin_info),
    ('^admin_info_add/$', admin_info_add),
    ('^admin_info_del/$', admin_info_del),
    ('^admin_info_update/$', admin_info_update),

    ('^admin_user/$', admin_user),
    ('^admin_user_active/$', admin_user_active),
    ('^admin_user_super/$', admin_user_super),
    ('^admin_user_del/$', admin_user_del),

    ('^loginpage/$', loginpage),
    ('^registerpage/$', registerpage),
    ('^login/$', login),
    ('^logout/$', logout),
    ('^register/$', register),

    ('^initdb/$', initdb),
)
# This will work if DEBUG is True
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
