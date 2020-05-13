
# What is the HOPE database?

This repo has 2 parts: first, we scrape a bunch of bibliogrpahical citation data, and o

A Quantitative History of Economic Research by Women (1940--2015)

# 5 Lines of Code to Replicate this Analysis?
- git clone  https://github.com/cbrunet93/HOPE
- cd HOPE
- docker pull ghislainv/docker-debian-jupyter.
 - docker run -d -p 8888:8888 -v ORIGIN_FOLDER:/home/dockeruser/notebooks ghislainv/docker-debian-jupyter
    - Replace ORIGIN_FOLDER with a folder on your local machine that you want to persist notebooks in.
    - Open your browser and start working with Jupyter notebook.
    - On Linux, the url will be localhost:8888.
    - On Windows/OSX, run docker-machine ip default (replace default with the name of your machine). Then, you'll be able to access     Jupyter notebook at CONTAINER_IP:8888.


# Release Timeline

v1.0 - May 10, 2020 - Initial Commmit
