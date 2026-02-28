import pytest
import requests
import allure
from jsonschema import validate
from data import POST_SCHEMA, fake_id, UPDATE_PAYLOADS


class TestPostsApi:

    @allure.title('Проверка получение одного поста по его ID (GET запрос)')
    @allure.description('Тест создает пост через фикстуру по его id получает его из базы данных')

    def test_get_single_post(self,base_url, api_session, post_for_del):
        target_id = post_for_del # Получаем ID из фикстуры

        with allure.step('Отправка GET запроса на получение созданного поста по его ID'):
            response = api_session.get(f"{base_url}/{target_id}")
            
            data = response.json()
            assert response.status_code == 200
            # Проверка структуры ответа
            assert data["id"] == target_id
            assert "title" in data
            assert "body" in data
            assert "userId" in data


    @allure.title('Проверка получения списка всех постов (GET запрос)')
    @allure.description('Тест получает список всех постов из базы данных')

    def test_get_all_post(self,base_url, api_session):

        with allure.step('Отправка GET запроса на получение списка всех постов'):
            response = api_session.get(f"{base_url}")
            posts = response.json()
            assert response.status_code == 200
            # роверка соответствия структуры через внешнюю схему
            validate(posts, POST_SCHEMA)

    @allure.title("Проверка успешного создания нового поста (POST)")
    @allure.description("Тест проверяет, что при отправке валидных данных , сервер создает пост и возвращает 201")
    def test_create_post_success(self, base_url, api_session, test_payload_and_delete_post):
        
        payload, id_clean = test_payload_and_delete_post
        with allure.step("Создание нового поста"):
            response = api_session.post(base_url, json=payload)

            created_post = response.json()
            new_id = created_post["id"] # получение id для удаления созданного поста
            id_clean["id"] = int(new_id) # Передаем ID в фикстуру для удаления

            assert response.status_code == 201
            assert created_post["title"] == payload["title"]
            assert created_post["body"] == payload["body"]
            assert created_post["userId"] == payload["userId"]


    @allure.title("Проверка успешного удаления существующего поста")
    @allure.description("Тест создает пост через фикстуру и проверяет, что DELETE запрос возвращает 200")
    def test_delete_post_success(self, base_url, api_session, post_for_del):
        target_id = post_for_del # Получаем ID из фикстуры
        
        with allure.step("Удаление созданного поста"):
            response = api_session.delete(f"{base_url}/{target_id}") 
        with allure.step("Попытка получения удаленного поста"):    
            check_response = api_session.get(f"{base_url}/{target_id}") # Запрос что поста больше нет
        
            assert response.status_code == 200
            assert check_response.status_code == 404
    
        
        

    @allure.title("Проверка удаления несуществующего поста")
    @allure.description("Тест проверяет, что DELETE запрос возвращает 404 с фейковым id ")
    def test_delete_fake_post(self, base_url, api_session):
        fake_id_post = fake_id
        with allure.step("Удаление несуществующего поста "):
            response = api_session.delete(f"{base_url}/{fake_id_post}")# запрос на удаление несуществующего поста
    
            assert response.status_code in [404]


    @allure.title("Проверка обновления существующего поста")
    @allure.description("Тест проверяет, что созданный пост обновляется новыми данными ")
    @pytest.mark.parametrize("payload_param", UPDATE_PAYLOADS)
    def test_update_post_put(self,base_url, api_session, test_payload_and_delete_post, payload_param):

        payload, id_clean = test_payload_and_delete_post
        with allure.step("Создаем новый пост"):
            response = api_session.post(base_url, json=payload)# создаем пост
            created_post = response.json()
            new_id = created_post["id"] # получение id для удаления созданного поста
            id_clean["id"] = int(new_id)# Передаем ID в фикстуру для удаления

        with allure.step("Обновляем созданный пост"):
            response_upd = api_session.put(f"{base_url}/{new_id}", json=payload_param)
            upd_post = response_upd.json()

            assert response_upd.status_code == 200
            assert upd_post["title"] == payload_param["title"]
            assert upd_post["body"] == payload_param["body"]
            assert upd_post["userId"] == payload_param["userId"]
        