ARG IMAGE_TAG=3.10-slim
FROM python:${IMAGE_TAG}

# Labels for docker image
LABEL maintainer="Anupam Yadav"
LABEL email="anupaminit@gmail.com"

# Arguments for docker file
ARG USERNAME=python
ARG GROUPNAME=$USERNAME
ARG USERID=1100
ARG GROUPID=$USERID

# Environment variable
# Prevents .pyc/__pycache__ creation
ENV PYTHONDONTWRITEBYTECODE=1
# Forces real-time logging/output (no buffering)
ENV PYTHONUNBUFFERED=1

# Check the current user and create a new user
RUN whoami
RUN groupadd --gid $GROUPID $GROUPNAME && useradd --uid $USERID --gid $GROUPID -m $USERNAME

# Copy requirements file and install all the required python packages
WORKDIR /app
COPY python/requirements.txt /app
# RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY python /app

# Install curl
RUN apt-get update && apt-get install -y curl

# Change the user to newly created user and run the processes as this user
USER $USERNAME
RUN whoami

# Expose the container port
EXPOSE 5001

# Change the working directory
WORKDIR /app

# Run the main application file on container startup
ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:5001", "--workers", "1", "--threads", "8", "run:app"]
