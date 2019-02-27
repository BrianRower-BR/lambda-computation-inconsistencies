#!/usr/bin/env bash

virtualenv -p python3.6 .Python
source ./.Python/bin/activate

rm -rf package
mkdir package
pushd package
pip install numpy --target .
pip install py-cpuinfo --target .
zip -r9 ../function.zip .
pushd ../src
zip -g ../function.zip main.py

# the process in based on this page:
# https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html