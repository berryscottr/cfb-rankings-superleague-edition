# provide password
ARG JUPYTER_TOKEN=''
ARG JUPYTER_PASSWORD=''
# get image with just jupyter and python installed
FROM jupyter/minimal-notebook
# copy repo to app directory on docker container
COPY . /app
# change directory to app
WORKDIR /app
# import project requirements
RUN pip3 install -r requirements.txt
# change directory to ranking code location
WORKDIR /app/src/ranking
# set jupyter password
#CMD ["jupyter", "notebook", "password"]
# run notebook without browser
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=${JUPYTER_TOKEN}", "--NotebookApp.password=${JUPYTER_PASSWORD}"]
