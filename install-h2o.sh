#!/bin/bash

VERSION=1.5.0

if [[ ! -d ./h2o ]]; then 
    mkdir ./h2o
fi

wget https://github.com/h2o/h2o/archive/v${VERSION}.tar.gz -O ./h2o/${VERSION}.tar.gz
{
    cd ./h2o
    tar xvfz ${VERSION}.tar.gz
}

{
    cd ./h2o/${VERSION}/h2o-${VERSION}
    cmake .
    make h2o
}
