FROM 99xt/scikit-base

MAINTAINER dilumnavanjana@gmail.com

#Install npm & nodejs
RUN apt-get update -y
RUN apt-get install nodejs npm -y

#Clone the WebApp Repo & update npm
RUN git clone https://github.com/99xt/scikit-api.git
WORKDIR scikit-api/web/ui
RUN npm install -g n
RUN n stable
RUN npm update
CMD npm start
