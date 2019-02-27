#!/usr/bin/env bash

FUNCTION_NAME="lambda-computation-inconsistencies"
ROLE_NAME="${FUNCTION_NAME}-role"

aws lambda delete-function --function-name ${FUNCTION_NAME} || echo "lambda did not exist"
aws iam delete-role-policy --role-name ${ROLE_NAME} --policy-name lambda-basic-execution
aws iam delete-role --role-name ${ROLE_NAME}
