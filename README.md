# khai-gis.info
A website for the department of geoinformation technology and space monitoring of the Earth.

## Локальная конфигурация для дебаггинга / разработки:
Перед началом - убедиться что установлены python 3.4, git, готов к использованию pip (менеджер библиотек для python). Если установлено несколько версий питона, переключится на 3.4
```
python --version
git --version
pip -V
```
(Если проблемы с pip - [можно сделать даунгрейд](https://stackoverflow.com/questions/62084243/pip-doesnt-work-after-upgrade-on-python-3-4-windows-10-how-to-downgrade) до рабочей на питоне 3.4.4 версии 19.1.1)
1. Создать [virtual environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) (виртуальную среду разработки):
```
virtualenv venv
```
2. Активировать новый virtual environment:
```
source venv/bin/activate
```
3. Установить в него пакеты из requirements.txt:
```
pip install -r requirements.txt
```
___

Следующие шаги предпринимаются перед непосредственно началом работы каждый раз при запуске проекта (как поднять сайт локально):

4. Активировать virtual environment:
```
source venv/bin/activate
```
5. Запустить сайт локально, использовав команду runserver в главном entry-pointе приложения - файле manage.py
```
python manage.py runserver
```
6. Перейти ссылку `http://127.0.0.1:8000/`, появившуюся в терминале. Чтобы *выключить* инстанс - `Ctrl+C`.

## Установка данных для администрирования, другие важные команды:
Создание суперюзера (для получения доступа в `http://127.0.0.1:8000/admin`):
```
python manage.py createsuperuser
```
Собрать статические файлы в рут папку (на сервере все статические файлы дублицируются и раздаются потом из этой папки):
```
python manage.py collectstatic
```
ЗАМЕТКА: Если на сайт была добавлена картинка / вордовский документ со ссылкой на него, и их не видно на сайте - скорее всего забыли собрать статические файлы.
