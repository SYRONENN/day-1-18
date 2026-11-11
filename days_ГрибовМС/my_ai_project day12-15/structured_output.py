import logging
from getpass import getpass
from gigachat import GigaChat
from pydantic import BaseModel, Field

fh = logging.FileHandler("app.log", encoding="utf-8")
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logging.basicConfig(level=logging.INFO, handlers=[fh])
class Result(BaseModel):
    category: str = Field(description="Категория сообщения")
    difficulty: str = Field(description="Сложность: низкая, средняя или высокая")
    score: int = Field(description="Оценка сложности от 1 до 10")
cert_path = "/home/student/Рабочий стол/days_Грибов/days_ГрибовМС/my_ai_project day12-15/my_project/certs"
key = getpass("Введите API ключ: ")
prompt = "Определи категорию и сложность вопроса: Как создать список в Python?"

try:
    with GigaChat(credentials=key, model="GigaChat-2", ca_bundle_file=cert_path) as client:
        completion, parsed = client.chat_parse(
            prompt,
            response_format=Result,
            strict=True
        )
        print("Категория:", parsed.category)
        print("Сложность:", parsed.difficulty)
        print("Оценка:", parsed.score)
        logging.info("Ответ получен")
except Exception as error:
    print("Не удалось получить структурированный ответ")
