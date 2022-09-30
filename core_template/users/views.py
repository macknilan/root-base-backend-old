from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from core_template.users.models import Profile
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = "users/user_detail.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's profile to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['profile'] = Profile.objects.filter(user=user)
        return context


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    # form_class: UserUpdateForm
    fields = [
        "first_name",
        "last_name",
        "phone_number",
    ]
    success_message = _("Information successfully updated")

    def get_form(self, *args, **kwargs):
        form = super(UserUpdateView, self).get_form(*args, **kwargs)
        form.fields["first_name"].widget.attrs.update(
            {"placeholder": "first name", "maxlength": 80, "required": True}
        )
        form.fields["last_name"].widget.attrs.update(
            {"placeholder": "last name", "maxlength": 80}
        )
        form.fields["phone_number"].widget.attrs.update(
            {"placeholder": "+00 (000) 000-000", "maxlength": 80}
        )
        # form.fields["email"].widget.attrs.update(
        #     {"disabled": True, "require": False, "readonly": True, "maxlength": 80}
        # )

        return form

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
