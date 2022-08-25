FROM python:3.9

LABEL author="Manoel JR"

WORKDIR /var/www/app

COPY requirements.txt /var/www/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /var/www/app/requirements.txt

COPY . /var/www/app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
