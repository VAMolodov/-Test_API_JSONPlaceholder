
base_url ='https://jsonplaceholder.typicode.com/posts' # базовый URL API JSONPlaceholder


post_data = {"title": "Test title","body": "Test body","userId": 1} # данные поста

fake_id = 99999 # фейковый id поста


# шаблон для списка постов
POST_SCHEMA = {"type": "array",  # Ожидаем список
            "items": { # Правила для каждого элемента внутри списка
            "type": "object",
            "properties": {"id": {"type": "number"},
                        "title": {"type": "string"},
                         "body": {"type": "string"},
                       "userId": {"type": "number"}
                          }
                 }
                  }
# данные для параметризированного теста
UPDATE_PAYLOADS = [
        {"title": "Updated Title", "body": "New content", "userId": 1},
        {"body": "Only updating body.", "userId": 5},
        {"title": "Only title updated.", "userId": 1}] 