FROM ubuntu

RUN apt update

RUN apt install python3 python3-pip -y

COPY requirements.txt /opt/app

WORKDIR /opt/app

RUN pip install -r requirements.txt

COPY . /opt/app

CMD python3 server.py