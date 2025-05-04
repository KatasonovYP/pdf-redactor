# ;encoding=utf-8
# Скрипт для замены слова "бюджетное" на "автономное" в тексте PDF

import re

import pdf_redactor

# Настройка параметров редактирования
options = pdf_redactor.RedactorOptions()

# Сохраняем исходные метаданные
options.metadata_filters = {
    "DEFAULT": [lambda value: value],  # Сохраняем все метаданные как есть
}

# Определяем замену слов
options.content_filters = [
    # Заменяем "бюджетное" на "автономное" (с учетом регистра)
    (
        re.compile(r"(бюджетное)"),  # Учитываем варианты с заглавной и строчной буквы
        lambda m: "автономное",
    ),
]

pdf_redactor.redactor(options)
