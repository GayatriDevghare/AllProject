from django.urls import path

from . import views


urlpatterns = [
    path('',views.GetBasePage),
    
    path('getregisterpage/',views.GetRegisterpage),
    path('getloginpage/',views.GetLoginpage),
    path('getemployeecurdpage/',views.GetEmployeecurdPage),
    path('getlogoutpage/',views.GetLogoutpage),
    path('gethomepage/',views.GETHomePage),
    path('getshowallpage/',views.GETShowAllPage),




    path('registeremployee/',views.RegisterEmployee),
    path('loginemployee/',views.LoginEmployee),
    path('logoutemployee/',views.LogoutEmployee),


    path('addemployee/',views.ADD_Employee),
    path('showsingleemployee/',views.Show_Single_Employee),
    path('deleteemployee/',views.Delete_Employee),
    path('updateemployee/',views.Update_Employee),
    path('deleteemployeeshowall/',views.DeleteEmployeeShowAll),

]