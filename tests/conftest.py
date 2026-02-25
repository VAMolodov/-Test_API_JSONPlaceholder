import pytest
import requests
from data import post_data, base_url


# Фикстура для создания и закрытия сессии requests
@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})

    yield session
    session.close()

# фикстура подготавливает данные для создания поста(пост не создает) 
# и удаляет созданный пост получая id поста из теста
@pytest.fixture
def test_payload_and_delete_post(api_session):
    payload = post_data
    id_clean = {}  # ID, которые нужно удалить

    yield payload, id_clean # Передаем данные для содания поста тесту

    post_id_del = id_clean.get("id")
    api_session.delete(f"{base_url}/{post_id_del}") # После выполнения теста, пытаемся удалить пост


# фикстура создает новый пост и возращает id созданного поста 
@pytest.fixture
def post_for_del(api_session):
    payload = post_data
    response = api_session.post(base_url, json=payload)
    post_id = response.json().get("id")
    
    return post_id  # Передаем ID в тест 

