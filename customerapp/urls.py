from django.urls import path 
from .views import *

urlpatterns = [
    path('home/', register_view),
    path('viewcustomer/', viewcustomer_view),
    path('update/', update_view),
    path('delete/', delete_view),
    path('login/', login_view),
    path('signup/', signup_view),
    path('logout/', logout_view),
    path('addcustomer/', addcustomer_view),
    path('viewbooking/', viewbooking_view),
    path('ajax/', ajax_view),
    path('state/', state_view),
    path('searchnames/', name_search_view),
    path('viewbills/', viewbills_view),
    path('printbill/', printbill_view),

]
