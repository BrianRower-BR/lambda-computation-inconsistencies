#!/usr/bin/env bash

FUNCTION_NAME="lambda-computation-inconsistencies"
ROLE_NAME="${FUNCTION_NAME}-role"
ZIP_PATH="function.zip"

# Create a new Role
echo "Create Role"
ROLE_RESULT=$(aws iam create-role --role-name "${ROLE_NAME}" --assume-role-policy-document file://trust-policy.json)
ROLE_ARN=$(echo ${ROLE_RESULT} | jq -r .Role.Arn)

# Attach a policy to that role
echo "Attach policy"
aws iam put-role-policy --role-name "${ROLE_NAME}" --policy-name lambda-basic-execution --policy-document file://lambda-execution-policy.json

sleep 10

# Create a lambda which uses the just created role
echo "Create lambda"
aws lambda create-function --function-name ${FUNCTION_NAME} --runtime python3.6 --role ${ROLE_ARN} --handler "main.lambda_handler" --zip-file "fileb://${ZIP_PATH}"