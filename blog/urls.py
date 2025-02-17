"""BodhiAI_Bog_Platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from blog import views
app_name='blog'
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'create_blog/',views.create_blog),
    url(r'^$', views.home, name='home',),
    url(r'^(?P<slug>[-\w]+)/$', views.entry, name='entry'),
    url(r'^categories/(?P<pk>\d+)/$', views.category_topics, name='category_topics'),
    url(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    #url(r'^(?P<pk>\d+)/comment/(?P<topic_pk>\d+)/$', views.comment),
    url(r'^add_comment/$',views.comment,name='comments'),
    #url(r'^tinymce/$', include('tinymce.urls')), 
    url(r'^title/(?P<pk>\d+)/$', views.get_title, name='get_title'),
]

