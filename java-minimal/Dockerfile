FROM inseefrlab/onyxia-base
ARG JAVA_VERSION=11

SHELL ["/bin/bash", "-c"]

ENV JAVA_HOME /usr/local/openjdk
ENV PATH $JAVA_HOME/bin:$PATH

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

USER root

RUN case $JAVA_VERSION in 11) URL=https://download.java.net/java/ga/jdk11/openjdk-11_linux-x64_bin.tar.gz;; 17) URL=https://download.java.net/java/GA/jdk17/0d483333a00540d886896bac774ff48b/35/GPL/openjdk-17_linux-x64_bin.tar.gz;; 20) URL=https://download.java.net/java/GA/jdk20/bdc68b4b9cbc4ebcb30745c85038d91d/36/GPL/openjdk-20_linux-x64_bin.tar.gz;; *) exit 1;; esac && echo $URL && wget --progress=dot:giga -O openjdk.tgz $URL; \
    mkdir -p "$JAVA_HOME"; \
    tar --extract \
		--file openjdk.tgz \
		--directory "$JAVA_HOME" \
		--strip-components 1 \
		--no-same-owner \
	; \
    rm openjdk.tgz*

USER 1000

CMD ["jshell"]
