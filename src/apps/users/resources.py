from import_export import resources
from .models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "date_joined",
        )
        export_order = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "date_joined",
        )
        import_id_fields = ("username",)
        skip_unchanged = True
        report_skipped = False
