from django.conf.urls import url
from . import views
# SET THE NAMESPACE!
app_name = 'startup'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='signup'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]