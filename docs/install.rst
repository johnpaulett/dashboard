Installation
============

::
    sudo apt-get install python-dev postgresql-server-dev-8.4 libxml2-dev libxslt-dev 

::
    mkdir $HOME/apps
    cd !$

    git clone git://github.com/johnpaulett/dashboard.git

    cd dashboard
    virtualenv --no-site-packages env
    source env/bin/activate
    easy_install pip
    env/bin/pip install -r requirements.txt

    
Deployment::

    sudo useradd --system --home-dir /home/dashboard --create-home dashboard --shell /bin/bash
    
    sudo -u postgres createuser -d -A -W -R dashboard
    sudo -u postgres createdb -O dashboard dashboard
