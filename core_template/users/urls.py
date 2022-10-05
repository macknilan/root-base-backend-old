from django.urls import path
from core_template.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_update_profile_view
)

app_name = "users"
urlpatterns = [
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("update/profile/", view=user_update_profile_view, name="update_profile"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
