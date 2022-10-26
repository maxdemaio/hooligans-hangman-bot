FROM python:3.9

WORKDIR .

COPY ./ .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8
ENV PYTHONPATH ./

CMD [ "python", "bot.py" ]