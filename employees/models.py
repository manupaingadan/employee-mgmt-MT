from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class DynamicForm(models.Model):
    """
    Represents a named form template (sections/fields stored in JSON).
    fields_json example:
    [
      {"label":"First name", "type":"text", "key":"first_name", "required": True},
      {"label":"Age","type":"number","key":"age","required": False}
    ]
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    fields_json = models.JSONField(default=list)  # stores array of field defs
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class EmployeeRecord(models.Model):
    """
    Stores employee data as JSON keyed by field.key from the DynamicForm.
    """
    form = models.ForeignKey(DynamicForm, on_delete=models.SET_NULL, null=True)
    data = models.JSONField(default=dict)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_employees')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        name = self.data.get('name') or self.data.get('first_name') or f'Employee {self.id}'
        return name
