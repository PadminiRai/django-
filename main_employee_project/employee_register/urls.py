from django.urls import path,include
from . import views
from .views import *
urlpatterns = [
    path('',views.employee_form ),
    path('list/',views.employee_list ),
    path('safety_ohs_a9/',safety_ohs_a9,name='safety_ohs_a9'),
    path('homepagef/',homepagef,name='homepagef'),
    path('charityregisterf/',charityregisterf,name='charityregisterf'),
    path('editschemef/',editschemef,name='editschemef'),
    path('acceptf/',acceptf,name='acceptf'),
   
]
