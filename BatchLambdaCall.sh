#!/bin/bash

for i in `seq 1 10`;
        do
            aws lambda invoke --function-name sandbox-inconsistent-results res.txt &
        done
