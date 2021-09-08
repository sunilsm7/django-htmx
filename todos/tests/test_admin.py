from todos.models import Todo
from todos.admin import TodoAdmin
from django.contrib.admin.sites import AdminSite
import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestTodoAdmin:
    def test_excerpt(self):
        site = AdminSite()
        todo_admin = TodoAdmin(Todo, site)
        obj = mixer.blend('todos.Todo', title='Buy milk from the market')
        result = obj.get_excerpt(8)
        assert result == 'Buy milk'
