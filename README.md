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


Using the zmq_server
--------------------
    
    bin/zmq_server -c 'tcp://0.0.0.0:5555'

Using the zmq_client
--------------------
  
    bin/zmq_client -m '<command>' -c 'tcp://<ip>:<port>'
    
/!\ You have to split the parameters in \<command\> with %, not spaces !
    
Example

    bin/zmq_client -m 'echo%hello%world' -c 'tcp://192.168.0.1:5555'
    



