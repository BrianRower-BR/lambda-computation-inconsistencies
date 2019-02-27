#!/usr/bin/env bash

FUNCTION_NAME="lambda-computation-inconsistencies"
rm -rf output
mkdir output
pushd output

for i in `seq 1 100`;
    do
        aws lambda invoke --function-name ${FUNCTION_NAME} res${i}.txt > /dev/null && cat res${i}.txt | jq .multiplied &
    done
