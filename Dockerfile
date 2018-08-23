FROM andrewosh/binder-base

MAINTAINER Raymond Speth <speth@mit.edu>

USER root

RUN conda install -n python3 -c cantera/label/dev -c cantera cantera

USER main
