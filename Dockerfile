FROM repo.asax.ir/repository/docker-bi-static/ubuntu:22.04

LABEL maintainer="M-Javad Heidarpour <djawad.dev@gmail.com>"

ARG update_package=0

ENV DEBIAN_FRONTEND=noninteractive


RUN sed 's|http://[^/]*.ubuntu.com|https://repo.asax.ir/repository|g' /etc/apt/sources.list > /etc/apt/sources.list.new && mv /etc/apt/sources.list.new /etc/apt/sources.list

RUN if [ $update_package -eq 0 ] ; then apt-get update \
  && apt-get install -y tzdata software-properties-common gcc build-essential python3 python3-pip \ 
  && apt-get autoremove -y  \
  && apt-get clean \
  && rm -rf /tmp/* /var/tmp/*; fi

COPY requirements.txt requirements.txt

ARG PYPI_REGISTRY_USER
ARG PYPI_REGISTRY_PASSWORD
ARG PYPI_REGISTRY

RUN pip --timeout=120 install --no-cache-dir -r requirements.txt  --index-url=https://${PYPI_REGISTRY_USER}:${PYPI_REGISTRY_PASSWORD}@${PYPI_REGISTRY}

# RUN groupadd -g 1001 chatbot && \
#    useradd -r -u 1001 -g chatbot chatbot

# RUN mkdir -p /app && chown chatbot:chatbot /app
# WORKDIR /app

# USER 1001

# COPY --chown=chatbot:chatbot . .

RUN mkdir -p /app
WORKDIR /app
COPY . .


EXPOSE 8100

CMD ["python3", "manage.py"]