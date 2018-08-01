from tuites.views import PostTuiteView
from django.urls import path

app_name = 'tuites'

urlpatterns = [
path('postar/', PostTuiteView.as_view(), name='post_tuite'),

]