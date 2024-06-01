# Select base image for the project
FROM cimg/python:3.12.3-node

# Choose what directory should be a working directory
# If the directory does not exist then Docker will create it
WORKDIR /app

# Copy project files into working directory
COPY /app /app

# Copy our local file with requirements into Docker Image
COPY requirements.txt ./

# Install all the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Set user
# RUN sudo groupadd -r das && useradd -r -g das sf

# Set permission
# RUN sudo chown -R circleci:circleci /app

#become user
USER root

# Open port for Docker
EXPOSE 3000

# Run flask
CMD flask run --host=0.0.0.0 --port=3000