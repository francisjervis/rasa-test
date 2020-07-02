FROM rasa/rasa-sdk:latest

USER root

WORKDIR /app

COPY actions.py /app

COPY requirements.txt /app

COPY aerobic-cosmos-271904-d4ee489f4625.json /app

RUN pip3 install -r requirements.txt

CMD ["start", "--actions", "actions"]

USER 1001