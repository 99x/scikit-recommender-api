FROM python

MAINTAINER dilumnavanjana@gmail.com

#Install scikit-learn with dependencies
RUN pip install -U numpy scipy scikit-learn

#Install Jupyter
RUN pip3 install --upgrade pip
RUN pip3 install jupyter
