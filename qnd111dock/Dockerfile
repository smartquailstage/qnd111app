FROM python:3.11-alpine
LABEL maintainer="support@smartquail.io"

ENV PYTHONUNBUFFERED 1

ENV NODE_VERSION=qnd111app
ENV NODE_APP_NAME=qnd111app
ENV USER=qnd111
ENV VERSION=111




RUN apk add --no-cache git
ARG username=smartquailDev
ARG password=ms1719183830
RUN git clone https://github.com/smartquailstage/${NODE_VERSION}.git


#COPY . /qnode0_app
#COPY ./qnode0_app.dev/qnode0_app_env_dev/qnode0_app/ /qnode0_app
COPY ./${VERSION}.txt /${VERSION}.txt
COPY ./scripts /scripts
COPY ./uwsgi_pro.ini /${NODE_VERSION}/${NODE_APP_NAME}/uwsgi_pro.ini
#COPY ./baton.min.js /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/baton.min.js
#COPY ./baton.min.js /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles/baton/app/baton/baton.min.js

COPY ./qnode_ascii-art.txt /${NODE_VERSION}/${NODE_APP_NAME}/qnode_art.txt

#COPY ./.env /qnode0.1_app/qnode01_app/.env 
#No olvidar sacar las variables de entorno.


WORKDIR /${NODE_VERSION}/${NODE_APP_NAME}
#EXPOSE 443 
#EXPOSE 25
EXPOSE 9000
#EXPOSE 587


RUN python3.11 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps && \
    apk add build-base curl  postgresql-dev gcc musl-dev python3-dev linux-headers && \
    rm -rf /var/lib/apt/lists/* && \
    apk add libffi-dev build-base py3-cffi py3-cryptography && \
    apk add jpeg-dev go   zlib-dev libjpeg build-base  wget  && \
    apk --update --upgrade --no-cache add fontconfig ttf-freefont font-noto terminus-font && \
    apk add gtk+3.0 pango && \
    apk add busybox-extras && \
    apk add openssl-dev && \
    apk add gettext && \
   # apk add screenfetch && \
    #/py/bin/pip install  rust  &&  \
    #/py/bin/pip install   py3-kiwisolver &&  \
    /py/bin/pip install -r /${VERSION}.txt && \
    apk del openssl-dev  &&  \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home ${USER} && \


  

    mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/static && \
   # mkdir -p /qnode0.0_app/qnode0_app/static/media && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/static  && \
    

    mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/media && \
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/media  && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/media && \
    
    mkdir -p /${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles && \
    chmod -R 755 /${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles  && \
    chown -R ${USER}:${USER} /${NODE_APP_NAME}/${NODE_APP_NAME}/staticfiles && \

    #chmod -R 755 /qnode0.0_app/qnode0_app/static/media  && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/static && \
    #chown -R qnode0:qnode0 /qnode0.0_app/qnode0_app/static/media && \
    #Uswgi
    
    mkdir -p  /var/log/uwsgi/ && \
    chown -R ${USER}:${USER} /var/log/uwsgi/ && \
    #GNUCORN
  #  mkdir -p /${NODE_VERSION}/${NODE_APP_NAME}/run/ && \
  #  mkdir -p /var/log/gunicorn &&\
  #  chown -R ${USER}:${USER} /var/log/gunicorn &&\
    
    chmod -R 755 /${NODE_VERSION}/${NODE_APP_NAME}/ && \
    
    chmod -R 755 /scripts  && \
   # chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/run/  && \
    chown -R ${USER}:${USER} /${NODE_VERSION}/${NODE_APP_NAME}/ &&\
 #   chmod -R 755 /var/log/gunicorn  && \
    
    #chmod -R u+x /scripts/gunicorn_run.sh &&\
    chmod -R u+x /scripts/uwsgi.sh &&\
    chmod -R +x /scripts 
    #rm /py/lib/python3.11/site-packages/baton/static/baton/app/dist/baton.min.js && \
    #cp /${NODE_VERSION}/${NODE_APP_NAME}/${NODE_APP_NAME}/baton.min.js  /py/lib/python3.11/site-packages/baton/static/baton/app/dist/ 



     
ENV PATH="/py/bin:/scripts:$PATH"

#COPY ./scripts/gunicorn.socket /qnode0.0_app/qnode0_app/run/

RUN apk add --no-cache --update musl musl-utils musl-locales tzdata
ENV TZ=America/Guayaquil
RUN cp /usr/share/zoneinfo/America/Guayaquil /etc/localtime

RUN echo 'export LC_ALL=es_ES.UTF-8' >> /etc/profile.d/locale.sh && \
    sed -i 's|LANG=C.UTF-8|LANG=es_ES.UTF-8|' /etc/profile.d/locale.sh

ENV LANG=es_ES.UTF-8 \
    LANGUAGE=es_ES.UTF-8
USER root
USER ${USER}

USER root
CMD ["uwsgi.sh"]


