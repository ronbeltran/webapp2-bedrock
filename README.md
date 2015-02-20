# webapp2-bedrock
Opinionated Webapp2 project template for Google App Engine

##To setup the project

    # clone the repo
    git clone git@github.com:ronbeltran/webapp2-bedrock.git

    # create a virtual env
    mkvirtualenv myproject

    #change to project dir
    cd webapp2-bedrock

    # install development requirements
    pip install -r dev_requirements

    # install needed third-party modules to lib dir
    pip install -r dev_requirements -t lib

    # run the dev server
    dev_appserver.py app.yaml
