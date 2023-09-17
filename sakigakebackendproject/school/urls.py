from .views import SchoolListView ,DetailView
from django.urls  import path
urlpatterns=[
    path('schools/',SchoolListView.as_view() , name='school_list'),
    path('schools/<int:school_id>/',DetailView.as_view() , name='school_detail'),
]