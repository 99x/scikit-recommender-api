FROM 99xt/scikit-base

MAINTAINER dilumnavanjana@gmail.com

#Install npm & nodejs
RUN apt-get update -y
RUN apt-get install nodejs npm -y && apt-get install -y supervisor

#install flask
RUN pip install flask

#update npm & node
RUN npm install -g n && n stable && npm update

#Clone the WebApp Repo & update npm
RUN git clone https://github.com/99xt/scikit-api.git && git checkout docker-dev

COPY scikit-api/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#Start web server
WORKDIR scikit-api/web/ui
#RUN npm install
#ENTRYPOINT python ../../server.py --no-daemon && npm start --no-daemon

# run supervisord
CMD ["/usr/bin/supervisord"]
