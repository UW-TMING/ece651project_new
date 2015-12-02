from django.conf.urls import include, url
from django.contrib import admin
from catelator import views
from catelator.views.UserView import *


user_patterns = [
    url(r'^index/$',views.UserView.index,name="index"),
    url(r'^go_register/$',views.UserView.go_register,name="go_register"),
    url(r'^register/$',views.UserView.register,name="register"),
    url(r'^go_login/$',views.UserView.go_login,name="go_login"),
    url(r'^logout/$',views.UserView.logout,name="logout"),
    url(r'^login/$',views.UserView.login,name="login"),
    url(r'^information/$',views.UserView.information,name="information"),
    url(r'^go_check_information/$',views.UserView.go_check_information,name="go_check_information"),
    url(r'^go_edit/(?P<user_id>\d+)/$',views.UserView.go_edit,name="go_edit"),
    url(r'^go_complete/(?P<user_id>\d+)/$',views.UserView.go_complete,name="go_complete"),
    url(r'^go_change_password/(?P<user_id>\d+)/$',views.UserView.go_change_password,name="go_change_password"),
    url(r'^go_change_password/(?P<user_id>\d+)/(?P<message>.+)/$',views.UserView.go_change_password,name="go_change_password"),
    url(r'^change_password/$',views.UserView.change_password,name="change_password"),
    url(r'^complete_information/$',views.UserView.complete_information,name="complete_information"),
    url(r'^edit_information/$',views.UserView.edit_information,name="edit_information"),
]

dish_patterns = [
    url(r'^go_dish_input/$',views.DishView.go_dish_input,name="go_dish_input"),
    url(r'^add/$',views.DishView.add,name="add"),
    url(r'^dish_list/$',views.DishView.dish_list,name="dish_list"),
    url(r'^edit/(?P<dish_id>\d+)/$',views.DishView.edit,name="edit"),
    url(r'^delete/(?P<dish_id>\d+)/$',views.DishView.delete,name="delete"),
    url(r'^update/$',views.DishView.update,name="update"),
    url(r'^show_detail/(?P<dish_id>\d+)/$',views.DishView.show_detail,name="show_detail"),
    url(r'^collect/(?P<dish_id>\d+)/$',views.DishView.collect,name="collect"),
    url(r'^like/(?P<dish_id>\d+)/$',views.DishView.like,name="like"),
]

home_patterns = [
    url(r'^$',views.HomeView.home,name="home"),
    url(r'^recipe/$',views.HomeView.recipe,name="recipe"),
]

test_patterns = [
    url(r'^test1/$',views.TestView.test1,name="test1"),
    url(r'^test2/$',views.TestView.test2,name="test2"),
    url(r'^test3/$',views.MonthlyWeatherByCityView.weather_chart_view,name="weather_chart_view"),
]

expectation_patterns = [
    url(r'^expecation_go_add/$',views.ExpectationView.go_add,name="go_add"), # to go to the add expectation page
    url(r'^deal_consumption/$',views.ExpectationView.deal_consumption,name="deal_consumption"),
    url(r'^expectation_add/$',views.ExpectationView.expectation_add,name="expectation_add"),
    url(r'^expectation_list/$',views.ExpectationView.expectation_list,name="expectation_list"),
    url(r'^delete/(?P<expectation_id>\d+)/$',views.ExpectationView.delete,name="delete"),# delete expectation
    url(r'^go_edit_expectation/(?P<expectation_id>\d+)/$',views.ExpectationView.go_edit,name="go_edit"),# to update expectation
    url(r'^expectation_edit/$',views.ExpectationView.edit,name="edit"),# to update expectation
]

reality_patterns = [
    url(r'^go_add_reality/(?P<expectation_id>\d+)/$',views.RealityView.go_add_reality,name="go_add_reality"), # to go to the add reality page
    url(r'^add_reality/$',views.RealityView.add_reality,name="add_reality"), # add Reality instance to the db
    url(r'^check_reality/(?P<expectation_id>\d+)/$',views.RealityView.check_reality,name="check_reality"), # check all Reality by expectation_id
]

urlpatterns = [
    url(r'^user/',include(user_patterns)),
    url(r'^dish/',include(dish_patterns)),
    url(r'^home/',include(home_patterns)),
    url(r'^test/',include(test_patterns)),
    url(r'^expectation/',include(expectation_patterns)),
    url(r'^reality/',include(reality_patterns)),
]
