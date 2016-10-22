FROM 99xt/scikit-base

MAINTAINER dilumnavanjana@gmail.com

#Install npm & nodejs
RUN apt-get update -y
RUN apt-get install nodejs npm -y

RUN pip install flask

RUN npm install -g n
RUN n stable
RUN npm update

#Clone the WebApp Repo & update npm
RUN git clone https://github.com/99xt/scikit-api.git

#Start python server
RUN python scikit-api/server.py &

#Start web server
WORKDIR scikit-api/web/ui
RUN npm install
CMD npm start
