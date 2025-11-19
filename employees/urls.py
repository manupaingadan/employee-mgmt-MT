from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DynamicFormViewSet, EmployeeRecordViewSet
from .views_page import login_page, formbuilder_page, employee_create_page,employee_list_page

router = DefaultRouter()
router.register(r'forms', DynamicFormViewSet, basename='forms')
router.register(r'employees', EmployeeRecordViewSet, basename='employees')


urlpatterns = [
    path("login/", login_page, name="login"),
    path('api/', include(router.urls)),

    path('formbuilder/', formbuilder_page, name='formbuilder'),
    path('employee/create/', employee_create_page, name='employee_create'),
    path('employees/', employee_list_page, name='employee_list'),

]

