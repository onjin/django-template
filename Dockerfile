FROM python:3.4-onbuild
ENV PYTHONUNBUFFERED 1

VOLUME /app/public/media

EXPOSE 80
EXPOSE 8000

CMD ["uwsgi", "uwsgi.ini"]
