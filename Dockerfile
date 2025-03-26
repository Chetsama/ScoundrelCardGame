FROM debian:latest

WORKDIR /usr/src

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    net-tools \
    iputils-ping \
    vim \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY main.py .

CMD ["python3", "main.py"]