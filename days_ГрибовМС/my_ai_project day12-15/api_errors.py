import os
from dotenv import load_dotenv
from gigachat import GigaChat
load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
cert_path = "/home/student/Рабочий стол/days_Грибов/days_ГрибовМС/my_ai_project day12-15/my_project/certs"
print("Пример с try и except")
try:
    with GigaChat(credentials=key, model="GigaChat-2", ca_bundle_file=cert_path) as client:
        response = client.chat.create("Привет")
        print(response.messages[0].content[0].text)
except Exception:
    print("Не удалось получить ответ от API")
print("\nПример с текстом ошибки")
try:
    with GigaChat(credentials=key, model="GigaChat-2", ca_bundle_file=cert_path) as client:
        response = client.chat.create("Привет")
        print(response.messages[0].content[0].text)
except Exception as error:
    print("Ошибка:", error)
print("\nПонятное сообщение пользователю")
try:
    with GigaChat(credentials=key, model="GigaChat-2", ca_bundle_file=cert_path) as client:
        response = client.chat.create("Привет")
        answer = response.messages[0].content[0].text
        print("Ответ:", answer)
except Exception as error:
    print("Не удалось выполнить запрос. Проверьте ключ и подключение.")
    print("Техническая информация:", error)
