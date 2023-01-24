from django.db import models
from django_filters import rest_framework, IsoDateTimeFilter

from goals.models import Goal


class GoalDateFilter(rest_framework.FilterSet):
    filter_overrides = {
        models.DateTimeField: {"filter_class": IsoDateTimeFilter},
    }

    class Meta:
        model = Goal
        fields = {
            "due_date": ("lte", "gte"),
            "category": ("exact", "in"),
            "status": ("exact", "in"),
            "priority": ("exact", "in"),
        }
