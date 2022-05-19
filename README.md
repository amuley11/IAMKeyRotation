# IAMKeyRotation
Lambda code for IAM key rotation


1. f-iam-key-manage.py --> A function to inactivate IAM users' existing key, create a new one and update it to the Secrets Manager

2. f-iam-key-delete.py --> A function to delete the inactivated key for IAM users

3. iam_policy.json --> A policy for Lambda's IAM role

4. IAM-Key-Rotation-Process.yaml --> CloudFormation template for deploying the entire module
