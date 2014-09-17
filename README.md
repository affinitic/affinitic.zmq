affinitic.zmq
=============

Install zmq
    sudo apt-get install libzmq3-dev

... or

    brew install zeromq

... or

    wget http://download.zeromq.org/zeromq-4.0.4.tar.gz
    tar -xvf zeromq-4.0.4.tar.gz
    cd zeromq-4.0.4/
    ./configure
    make
    sudo make install
    sudo ldconfig
    cd ..
    rm -rf zeromq-4.0.4.tar.gz zeromq-4.0.4/

Zmq python library will need python-dev

    sudo apt-get install python-dev


Using the zmq_server:
------------------------
    
    bin/zmq_server

Using the zmq_client:
------------------------
  
    bin/zmq_client '<command>' 'tcp://<ip>:<port>'
    



