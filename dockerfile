# start from an official image
FROM python:3.7

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/coronacircles
WORKDIR /opt/services/coronacircles

# install our dependencies
COPY ./requirements.txt /opt/services/coronacircles/requirements.txt
RUN pip install -r requirements.txt

# copy our project code
COPY ./ /opt/services/coronacircles/

# expose the port 8000
EXPOSE 8000