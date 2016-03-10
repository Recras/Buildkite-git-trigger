FROM python:2-onbuild

RUN useradd -m flask

EXPOSE 5000

USER flask
WORKDIR /home/flask

CMD [ "python", "/usr/src/app/builder.py" ]
