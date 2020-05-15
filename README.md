
# What is the HOPE database?

TBD

# 4 Lines of BASH to Replicate 

1. git clone  https://github.com/cbrunet93/HOPE
2. cd HOPE

NOTE: DOCKER IS BROKEN/NOT WORKING YET 

3. docker pull ghislainv/docker-debian-jupyter.
4.  docker run -d -p 8888:8888 -v ORIGIN_FOLDER:/home/dockeruser/notebooks ghislainv/docker-debian-jupyter
    - Replace ORIGIN_FOLDER with a folder on your local machine that you want to persist notebooks in.
    - Open your browser and start working with Jupyter notebook.
    - On Linux, the url will be localhost:8888.
    - On Windows/OSX, run docker-machine ip default (replace default with the name of your machine). Then, you'll be able to access     
    Jupyter notebook at CONTAINER_IP:8888.

# To-Do

1. Make a better README file

# Release Timeline

v1.0 - May 10, 2020 - Initial Commmit
