
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from.import views

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home, name = 'home'),

    path('<int:id>/', views.detail, name ='detail'),

    path('<int:id>/update/', views.update, name='update'),

    path('new/',views.new_form, name='add_new'),

    path('login/',views.login_req, name ='login'),

   # path('login/', views.login, name='login'),

    path('signup/', views.signup, name='signup'),

    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('delete/<int:id>', views.delete, name='delete'),

]
