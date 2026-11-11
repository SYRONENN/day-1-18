import os
from dotenv import load_dotenv
from gigachat import GigaChat
from prompts import SYSTEM_PROMPT
from gigachat.models import ChatCompletionRequest, ChatMessage
load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")
question = input("Напишите, какие примерно фильмы вам нравятся (жанр, год, с кем хотите смотреть)").strip()
request = ChatCompletionRequest(
    messages=[
        ChatMessage(
            role= "system",
            content=SYSTEM_PROMPT,
        ),
        ChatMessage(
            role="user",
            content=question,
        )
    ]

)
print("Отправляем запрос...")
with GigaChat(
    credentials=key,
    scope=scope,
    model="Gigachat-2",
    ca_bundle_file="/home/student/Рабочий стол/days_Грибов/days_ГрибовМС/my_ai_project day12-15/my_project/certs/Russian_Trusted_Root_CA.cer",
    timeout=60,
) as client:
    response = client.chat.create(request)
answer = response.messages[0].content[0].text
print("Ответ:")
print(answer)