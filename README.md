# Рекомендационная система для подбора фильмов на основе текстовых описаний
## 1. Проект выполнил
* Лакеев Денис Максимович
* Группа 22БАЭМ

## 2. Описание
Используя методы обработки естественного языка (NLP) и алгоритмы машинного обучения, система анализирует текстовые описания фильмов и предоставляет персонализированные рекомендации с учетом предпочтений пользователя. Проект использует возможности NLP для извлечения ключевых характеристик и информации из описаний фильмов. Система обрабатывает текстовые данные, дабы выделить основные темы, краткое описание сюжета и другую важную информацию. Улавливая суть каждого фильма, система может выявлять сходства и закономерности, которые ложатся в основу алгоритма рекомендаций.

Для создания системы рекомендаций была собрана обширная база данных фильмов, содержащая названия, описания, жанры и другие необходимые метаданные. Данные были собраны с помощью **_парсинга_** (aiohttp, asyncio, beautifulsoup) известной базы с кинематографом.

Текст трансформируется в вектор с помощью TF-IDF:

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*V9ac4hLVyms79jl65Ym_Bw.jpeg">
</p>

## 3. Техническое описание
* Версия Python: 3.8.8
* Необходимые библиотеки могут быть установлены с помощью файла _requirements.txt_

## 4. Структура проекта
* /configs - скрытая папка с конфигом к личному серверу;
* /data - папка с данными в csv формате;
* eda.ipynb - нотбук с анализом собранных данных;
* load_data.py - выгрузка данных в csv формат;
* main.ipynb - нотбук с рекомендационной системой;
* requirements.txt - файл с названиями и версиями используемых в проекте библиотек.

## 5. Способы улучшения
```diff
+ Добавление информации об оценках пользователя фильмов, которые он уже видел.

+ Добавление нескольких пользователей для подбора фильмов по схожести интересов.

+ Более детальное описание кинематографа (возможно информация о рецензиях).
```
