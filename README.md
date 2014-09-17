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

Add this line to your .bashrc / .zshrc this will allow virtuaenv to use dist-packages

    export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages:/usr/local/lib/python2.7/dist-packages
    
Add this line to your .bashrc / .zshrc this allow python script to access configuration file. See the sms.cfg_example for the syntax

    export SMS_CONFIG_PATH=/home/<user>/buildout/affinitic.smsutils/sms.cfg

/!\ Make sure the zmq\_server is working before launching the zmq_client

Using the zmq_server:
    
    bin/zmq_server

Using the zmq_client:
  
    bin/zmq_client '<command>'
    
ie:/home/<user>/buildout/affinitic.ircutils/bin/send\_irc_message|-s|hyperflix.net|-n|alibabot|-c|#ircNoob|-m| hello world|-p|6667


