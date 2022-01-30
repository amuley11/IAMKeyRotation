# IAMKeyRotation
Lambda code for IAM key rotation


f-iam-key-manage.py --> A function to inactivate IAM users' existing key, create a new one and update it to the Secrets Manager
f-iam-key-manage.py --> A function to delete the inactivated key for IAM users
iam_policy.json --> A policy for Lambda's IAM role
