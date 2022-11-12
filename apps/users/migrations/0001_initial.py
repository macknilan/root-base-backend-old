# Generated by Django 4.1.3 on 2022-11-12 18:49

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date time at which an object was created", verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, help_text="Date time at which an object was modified", verbose_name="modified"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        error_messages={"unique": "A user with that email already exists."},
                        max_length=255,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: +00 (000) 000-0000",
                                regex="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$",
                            )
                        ],
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(default=True, help_text="Public profiles show all information about users."),
                ),
                (
                    "is_verified",
                    models.BooleanField(
                        default=False,
                        help_text="Determine if an user has a verified account. Set to true when user verified its email address.",
                        verbose_name="verified",
                    ),
                ),
                (
                    "is_client",
                    models.BooleanField(
                        default=True,
                        help_text="Help easily distinguish users and perform queries. Clients are the main type of user.",
                        verbose_name="client",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Date time at which an object was created", verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, help_text="Date time at which an object was modified", verbose_name="modified"
                    ),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="users_pictures/", verbose_name="profile picture"
                    ),
                ),
                (
                    "biography",
                    models.TextField(
                        default="Update your bio ...",
                        help_text="A small biography about the user",
                        max_length=500,
                        verbose_name="About your profile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "ordering": ["-created", "-modified"],
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
    ]
