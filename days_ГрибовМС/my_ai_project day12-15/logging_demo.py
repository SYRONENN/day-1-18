import logging

fh = logging.FileHandler("app.log", encoding="utf-8")
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logging.basicConfig(level=logging.INFO, handlers=[fh])
logging.info("Программа запущена")
logging.info("Получен запрос")
logging.warning("Пользователь ввёл пустой текст")
logging.error("Не удалось обратиться к API")
