FROM python:3.9

WORKDIR .

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8
ENV PYTHONPATH ./

COPY ./ .

CMD [ "python", "bot.py" ]