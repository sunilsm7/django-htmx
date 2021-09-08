import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestTodo:
    def test_model(self):
        obj = mixer.blend('todos.Todo')
        assert obj.pk == 1, 'Should create a todo instance'

    def test_excerpt(self):
        obj = mixer.blend('todos.Todo', title='Buy milk from the market')
        result = obj.get_excerpt(8)
        assert result == 'Buy milk'