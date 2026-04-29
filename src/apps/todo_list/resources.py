from import_export import resources
from .models import Todo


class TodoResource(resources.ModelResource):
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
