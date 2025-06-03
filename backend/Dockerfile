FROM docker.io/python:3.13

COPY ./requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN ["chmod", "+x", "./startup.sh"]

CMD "./startup.sh"
