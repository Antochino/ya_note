import pytest

from notes.models import Note

@pytest.fixture
# Используем встроенную фикстуру для модели пользователей django_user_model.
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')

@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


@pytest.fixture
def note(author):
    note = Note.objects.create(
        title='title',
        text='text',
        slug='no-slug',
        author=author,
    )
    return note

@pytest.fixture
# Фикстура запрашивает другую фикстуру создания заметки.
def slug_for_args(note):
    # И возвращает кортеж, который содержит slug заметки.
    # На то, что это кортеж, указывает запятая в конце выражения.
    return note.slug,


# Добавляем фикстуру form_data
@pytest.fixture
def form_data():
    return {
        'title': 'Новый заголовок',
        'text': 'Новый текст',
        'slug': 'new-slug'
    }