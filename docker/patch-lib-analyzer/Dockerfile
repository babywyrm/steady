FROM openjdk:8-jre-alpine

LABEL maintainer="steady-dev@eclipse.org"

ARG VULAS_RELEASE

COPY patch-lib-analyzer-${VULAS_RELEASE}-jar-with-dependencies.jar /vulas/patch-lib-analyzer.jar
COPY run.sh /vulas/run.sh

RUN chmod +x /vulas/run.sh

CMD ["/vulas/run.sh"]
