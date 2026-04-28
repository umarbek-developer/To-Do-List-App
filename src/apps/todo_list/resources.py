from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth import get_user_model
from .models import Todo

User = get_user_model()


class TodoResource(resources.ModelResource):
    user = fields.Field(
        column_name="user",
        attribute="user",
        widget=ForeignKeyWidget(User, field="email"),
    )

    class Meta:
        model = Todo
        fields = (
            "id",
            "user",
            "title",
            "desc",
            "is_completed",
            "deadline",
            "created_at",
        )
        export_order = (
            "id",
            "user",
            "title",
            "desc",
            "is_completed",
            "deadline",
            "created_at",
        )
        import_id_fields = ("id",)
        skip_unchanged = True
        report_skipped = False
