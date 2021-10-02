from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import *
app_name="crud"
urlpatterns = [
    # path('chart/', chart, name='index'),
    path('', permission_required('is_staff')(ProductList.as_view()), name="home"),
    path('add/', permission_required('is_staff')(Productcreate.as_view()),name="create"),
    path('<pk>/update/', permission_required('is_staff')(ProductUpdateView.as_view()), name="productedit"),
    path('<pk>/delete/', permission_required('is_staff')(ProductDeleteView.as_view()), name="productdelete"),
    path('categorylist/', permission_required('is_staff')(CategoryList.as_view()), name="categorylist"),
    path('addcategory/', permission_required('is_staff')(CategoryAddView.as_view()),name="categorycreate"),
    path('<pk>/categoryupdate/', permission_required('is_staff')(CategoryUpdateView.as_view()), name="categoryedit"),
    path('<pk>/categorydelete/', permission_required('is_staff')(CategoryDeleteView.as_view()), name="categorydelete"),
    path('orderlist/', permission_required('is_staff')(OrderList.as_view()), name="order"),
    path('<pk>/Orderupdate/', permission_required('is_staff')(OrderUpdateView.as_view()), name="orderedit"),
]