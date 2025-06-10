# Use the latest debian, this is large and could be swapped for a python image
FROM debian:latest

# Set the working directory in the container
WORKDIR /usr/src

# install various dependencies
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

# Copy the file main.py (use . for current directory contents) into /usr/src/ 
COPY main.py .

# Run the command "python3 main.py" 
CMD ["python3", "main.py"]
