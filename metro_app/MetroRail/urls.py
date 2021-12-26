"""MetroRail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Ticket import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Ticket),
    path('Fare/', views.Fare),
    path('Complains/', views.Complains),
    path('AfterComplain/', views.AfterComplain, name="AfterComplain"),
    path('SeeComplains/', views.SeeComplains),
    path('BuyTickets/', views.BuyTickets,name="BuyTickets"),
    path('AfterTickets/', views.AfterTickets, name="AfterTickets"),
    path('CancelTickets/', views.CancelTickets,name="CancelTickets"),
    path('AfterCancelTickets/', views.AfterCancelTickets, name="AfterCancelTickets"),
    path('PostponeTickets/', views.PostponeTickets,name="PostponeTickets"),
    path('AfterPostponeTickets/', views.AfterPostponeTickets, name="AfterPostponeTickets"),
    path('TicketMenu/', views.TicketMenu,name="TicketMenu"),

]
