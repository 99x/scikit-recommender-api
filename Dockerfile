FROM 99xt/scikit-base

MAINTAINER dilumnavanjana@gmail.com

#Install npm & nodejs
RUN apt-get update -y && apt-get install nodejs npm supervisor -y

#install flask
RUN pip install flask

#update npm & node
RUN npm install -g n && n stable && npm update

#Clone the Repo
RUN git clone https://github.com/99xt/scikit-api.git

#Copy supervisor.conf file from repo
COPY scikit-api/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#npm install
WORKDIR scikit-api/web/ui
RUN npm install
WORKDIR ../../../

EXPOSE 8080

# run supervisord
ENTRYPOINT ["/usr/bin/supervisord"]
