FROM debian:wheezy


RUN apt-get update

#install git
RUN apt-get install -y  git-core


#install python



RUN apt-get install -y python


RUN cd /home/; git clone https://github.com/affinitic/affinitic.smsutils.git
RUN cd /home/; git clone https://github.com/affinitic/affinitic.zmq.git;
ADD  https://bootstrap.pypa.io/bootstrap-buildout.py  /home/affinitic.smsutils/bootstrap.py
ADD  https://bootstrap.pypa.io/bootstrap-buildout.py  /home/affinitic.zmq/bootstrap.py
RUN cd /home/affinitic.smsutils/; python bootstrap.py; bin/buildout
RUN apt-get install -y python2.7-dev
RUN apt-get install -y g++
RUN cd /home/affinitic.zmq/; python bootstrap.py; bin/buildout
ENV PYTHONPATH=":/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages"
CMD cd /home/affinitic.zmq/; bin/zmq_server -c 'tcp://0.0.0.0:5555'
