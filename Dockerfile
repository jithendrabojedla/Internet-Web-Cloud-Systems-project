# Use Google Cloud SDK's container as the base image
FROM google/cloud-sdk

# Specify your e-mail address as the maintainer of the container image
LABEL maintainer="jbojedla@pdx.edu"

# Copy the contents of the current directory into the container directory /app
COPY . /app

# Set the working directory of the container to /app
WORKDIR /app

# Install Python and pip inside the container
RUN apt-get update -y && apt-get install -y python3 python3-venv python3-pip

# Create a virtual environment and activate it
RUN python3 -m venv /app/venv
RUN /bin/bash -c "source /app/venv/bin/activate && pip install -r requirements.txt"

# Set environment variable to use the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Set the parameters to the program
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

