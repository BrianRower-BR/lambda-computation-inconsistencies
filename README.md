# lambda-computation-inconsistencies

This repository contains code to demonstrate that it is possible
to get different calculation results with the same code
run on AWS Lambda many times. 

## Dependencies:
* a linux machine (tested on ubuntu 18.04)
* The following utilities must be installed and in your command line PATH:
    - python3.6
    - virtualenv
    - "jq" (sudo apt get install jq)
    - aws command line (configured with valid default credentials)
    
## Setup the Lambda:
1. git clone https://github.com/BrianRower-BR/lambda-computation-inconsistencies.git
2. cd lambda-computation-inconsistencies
3. ./package.sh
    - this creates "function.zip" the lambda code package w/ numpy and cpuinfo installed
4. ./createLambda.sh
    - this will create a role named "lambda-computation-inconsistencies-role"
        - the role will have the trust policy in "trust-policy.json"
        - the role will have the policy in "lambda-execution-policy.json"
    - this will create a lambda named "lambda-computation-inconsistencies" using "function.zip" for the code

## Execute the test:
1. Via terminal, execute: "./run.sh"

This script will run the newly created lambda 100 times
All the runs get started in the background, so after 
executing run.sh it will appear that nothing happened
...just wait.
When the lambdas begin to complete, they will output their result to the terminal.
If you scroll through the output you will see that not all the numbers are the same.
At last execution we saw the following two values:
* 797.1493585088962
* 797.1493585088965

## Cleanup
1. Via terminal, execute: "./cleanup.sh"