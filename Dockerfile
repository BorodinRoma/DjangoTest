# Используем официальный образ Python в качестве базового образа
FROM python
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/django_rest_test

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/

RUN pip install -r /usr/src/requirements.txt


COPY . /usr/src/django_rest_test

EXPOSE 8000
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]