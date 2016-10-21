FROM ruimashita/numpy

MAINTAINER dilumnavanjana@gmail.com

#Install scikit-learn with dependencies
RUN pip install -U numpy scipy scikit-learn

#Install Jupyter
RUN pip install jupyter
