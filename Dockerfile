FROM python:3.10
LABEL maintainer="Mykola Nosenko (mnosenko@freeadmin.pp.ua)"
ENV APP_RETURN_DATA_SIZE 100
ENV APP_WAIT_TIME_TO_RESPONSE 10
ENV FLASK_APP govnoloader
ENV FLASK_DEBUG 0
ENV FLASK_ENV production
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN rm /requirements.txt
WORKDIR /app
COPY app/ .
CMD ["flask", "run", "-h", "0.0.0.0"]
