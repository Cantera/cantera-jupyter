FROM andrewosh/binder-base

MAINTAINER Raymond Speth <speth@mit.edu>

USER root

RUN conda install -n python3 -c bryanwweber/channel/devel cantera

USER main
