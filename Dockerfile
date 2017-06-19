FROM centos:7

LABEL name="rabbitmq-test-client"

RUN yum -y install epel-release && \
    yum -y install python-pip && \
    yum clean all

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./docker-entrypoint.sh /
COPY ./scripts /scripts

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python"]

