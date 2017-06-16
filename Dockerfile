FROM python:3
RUN pip install uwsgi
RUN mkdir /sockets
ADD requirements.txt /
RUN pip install -r /requirements.txt
COPY uwsgi.ini /etc/uwsgi/
COPY src/ /app
WORKDIR /app
CMD /usr/local/bin/uwsgi --ini /etc/uwsgi/uwsgi.ini --ini /app/uwsgi.ini
