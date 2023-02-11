from django.contrib import admin
from core.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CostumUserCreationForm, CustomUserChangeForm


class CostumUserAdmin(BaseUserAdmin):
    add_form = CostumUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("rolle","email", "is_staff", "is_active", "is_superuser", "is_admin", "is_tutor", "is_kursleiter",)
    list_filter = ("rolle","email", "is_staff", "is_active", "is_superuser","is_admin", "is_tutor", "is_kursleiter",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("rolle", "is_staff", "is_active", "is_superuser", "is_admin", "is_tutor", "is_kursleiter", 
        "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "rolle", "is_staff",
                "is_active",  "is_superuser","is_admin", "is_tutor", "is_kursleiter", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

# User-View
# class UserAdminConfig(UserAdmin):
#     list_display = ('id', 'email', 'vorname', 'nachname', 'role', 'date_published', 'date_modified', )
#     list_filter = ('role',)
#     ordering = ('email',)

#     fieldsets = (
#         (None, {'fields':('email', 'vorname', 'nachname', 'role', )}),
#         ('Permissions', {
#             'fields': (
#                 'groups',
#                 ),
#         }),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide'),
#             'fields': ('email', 'vorname', 'nachname','groups', 'role', 'password1', 'password2', )
#         }),
#     )


# # Teacher-View
# class KursleiterView(UserAdmin):
#     list_display = ('email', 'vorname', 'nachname',  'role', 'kurs_name',)
#     list_filter = ('kurs_name',)
#     ordering = ('email', )

#     fieldsets = (
#         (None, {'fields':('vorname', 'nachname', 'email', 'role', 'kurs_name', )}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide'),
#             'fields': ('email', 'vorname', 'nachname', 'role', 'kurs_name', 'password1', 'password2', )
#         }),
#     )


# class TutorView(UserAdmin):
#     list_display = ('email', 'vorname', 'nachname', 'tutor_id', 'role', 'kurs_name', 'arbeitsstunden', )
#     list_filter = ('email', 'vorname', 'nachname', )
#     ordering = ('email', )

#     fieldsets = (
#         (None, {'fields':('email', 'vorname', 'nachname', 'role', 'tutor_id', 'kurs_name', 'arbeitsstunden',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide'),
#             'fields': ('email', 'vorname', 'nachname','role', 'tutor_id', 'kurs_name', 'arbeitsstunden', 'password1', 'password2', )
#         }),
#     )


# class KursView(admin.ModelAdmin):
#     list_display = ('kurs_name', 'dozent',)

# class ProfileView(admin.ModelAdmin):
#     list_display = ('email')


admin.site.register(User, CostumUserAdmin) # UserConfigAdmin

admin.site.register(Dozent)
admin.site.register(DozentProfile)

admin.site.register(Kursleiter, CostumUserAdmin) # , KursleiterView
admin.site.register(KursleiterProfile)

admin.site.register(Tutor, CostumUserAdmin) # , TutorView
admin.site.register(TutorProfile)

admin.site.register(Kurs) # , KursView
admin.site.register(Blatt)
