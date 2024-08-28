ARG BASE_IMAGE=liaslaboratory/onyxia-java-minimal
FROM $BASE_IMAGE

LABEL maintainer="Mickael BARON <baron@ensma.fr>"

SHELL ["/bin/bash", "-c"]

ENV MAVEN_HOME=/usr/local/maven
ENV PATH=$MAVEN_HOME/bin:$PATH

USER root

ENV MAVEN_LINK=https://dlcdn.apache.org/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz
RUN wget --progress=dot:giga -O maven.tgz $MAVEN_LINK; \
    mkdir -p "$MAVEN_HOME"; \
    tar --extract \
                --file maven.tgz \
                --directory "$MAVEN_HOME" \
                --strip-components 1 \
                --no-same-owner \
        ; \
    rm maven.tgz*

USER 1000