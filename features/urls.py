from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('volunteer',views.volunteer,name="volunteer"),
    path('causes',views.causes,name="causes"),
    path('causes/<int:pk>',views.causes_detail,name='causes_detail'),
    path('blog',views.blog,name="blog"),
    path('blog/<int:pk>',views.blog_detail,name='blog_detail'),
    path('contact',views.contacts,name="contact"),
    path('gallery',views.pics,name="gallery"),
    path('events',views.event,name="events"),
    path('events/<int:pk>',views.events_detail,name='events_detail'),
]
