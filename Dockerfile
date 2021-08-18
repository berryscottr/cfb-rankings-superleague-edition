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
# run notebook without browser
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
