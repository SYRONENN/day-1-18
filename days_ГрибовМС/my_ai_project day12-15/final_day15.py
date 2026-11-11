import os
import logging # запись логов и ошибок
from dotenv import load_dotenv # загрузка ключей
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions #формирование запросов
from prompts import SYSTEM_PROMPT

#достаем ключи из .енв и настраиваем запись логов
load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = logging.FileHandler("app.log", encoding="utf-8") # файл для сохранения логов
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")) #формат записи с временем уровнем и текстом
logger.addHandler(fh)

print("Помощник по выбору фильмов")
print("Команды управления")
print("'выход' - завершить работу")
print("'очистить' - начать новый разговор (сбросить историю)")
print("'история' - посмотреть текущее состояние памяти чата\n")

messages = [
    ChatMessage(
        role="system",
        content=SYSTEM_PROMPT,
    )
]

logging.info("Программа запущена")

#подключаемся к гигачату с ключом и сертификатом
with GigaChat(
    credentials=key, #передаем ключ
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="/home/student/Рабочий стол/days_Грибов/days_ГрибовМС/my_ai_project day12-15/my_project/certs/Russian_Trusted_Root_CA.cer",
    timeout=60,
) as client:
    #запускаем бесконечный цикл диалога с пользователем
    while True:
        raw_input = input("\nНапишите ваши предпочтения и я выберу фильм специально для вас или введите команду: ")
        command_candidate = raw_input.strip().lower()

        #проверяем не ввел ли пользователь команду выхода очистки или истории
        if command_candidate == "выход":
            logging.info("Пользователь завершил работу")
            print("До свидания")
            break
        if command_candidate == "очистить":
            messages = [messages[0]]
            logging.info("История диалога очищена")
            print("\n[История диалога очищена.]")
            continue
        if command_candidate == "история":
            print(f"\nКоличество сообщений в истории: {len(messages)}")
            print("Роли сообщений по порядку:")
            for msg in messages:
                print(f"роль: {msg.role}")
            continue
        #пустой ввод
        if not raw_input.strip():
            logging.warning("Пользователь ввёл пустой текст")
            print("\nошибка: пустое сообщение")
            continue

        #добавляем сообщение пользователя в историю
        logging.info("Получен пользовательский запрос")
        messages.append(
            ChatMessage(
                role="user",
                content=raw_input.strip(),
            )
        )

        #параметры запроса к модели
        request = ChatCompletionRequest(
            model="GigaChat-2",
            messages=messages,
            model_options=ChatModelOptions(
                temperature=0.2, #температура
                max_tokens=300 #длина
            )
        )
        print("\nОтправляем запрос...")
        logging.info("Запрос отправлен")
        #отправляем запрос в api
        try:
            response = client.chat.create(request)
            answer = response.messages[0].content[0].text

            print("\nОтвет от ИИ-помощника:")
            print(answer)

            messages.append(
                ChatMessage(
                    role="assistant",
                    content=answer,
                )
            )
            logging.info("Ответ получен")
            logging.info("Запрос к API выполнен успешно")

            print(f"Длина истории сообщений: {len(messages)}")

            if len(messages) > 7: # проверяем не превысила ли история лимит в семь сообщений
                messages = [messages[0]] + messages[-6:]
                logging.info("История обрезана")
        #ошибки если апи не работает или нет сети
        except Exception as e:
            logging.error("Ошибка API: %s", e)
            print("Не удалось выполнить запрос. Проверьте ключ и подключение.")