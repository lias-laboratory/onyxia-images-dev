FROM inseefrlab/onyxia-base
ARG ADA_VERSION=12.3.0

LABEL maintainer="Mikky Richard richardm@mikkyrichard.fr"

# SHELL ["/bin/bash", "-c"]
USER root

# Update and Locales
RUN \
    apt-get update --yes &&\
    apt-get full-upgrade --yes &&\
    apt-get install --no-install-recommends --yes \
    locales
ENV LANG=C.UTF-8
ENV LANGUAGE=fr_FR:en
ENV LC_ALL=C.UTF-8

# Base tools
RUN \
    apt-get install --no-install-recommends --yes \
    zsh \
    vim nano \
    zip bzip2 gzip tar \
    curl wget dirmngr file tree

# Dev tools
RUN \
    apt-get install --no-install-recommends --yes \
    autogen automake bash bc bison \
    build-essential \
    make gdb nasm \
    gcc-11 gcc-12
    
    # Gnat
    RUN \
    apt-get install --no-install-recommends --yes \
    gnat-12

# Clean
RUN \
    apt-get clean autoclean --yes \
    && apt-get autoremove --yes 
#    && rm -fr /var/lib/{apt,dpkg,cache,log}/
#    && rm /etc/ssh/*key*

USER 1000
RUN \
    echo 'export PS1="🐳 %F{blue}Ada-minimal %f %~ > "' >> /home/onyxia/.zshrc && \
    echo 'export PS1="🐳 %F{blue}Ada-minimal %f %~ > "' >> /home/onyxia/.bashrc
ENV SHELL=/usr/bin/zsh
WORKDIR /Ada-Workspace
# RUN /bin/zsh /root/.zshrc

CMD ["/bin/zsh" "/root/.zshrc"]