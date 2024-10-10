# Automating Data Processing with AWS Lambda and S3

## Project Overview
This project automates the processing of files uploaded to an S3 bucket using AWS Lambda. Whenever a file is uploaded to the Source S3 bucket, the Lambda function is triggered to process the file (converting text to uppercase) and stores the result in a Destination S3 bucket.

## Tools Used
- AWS Lambda
- AWS S3
- AWS CloudWatch
- Python

## Steps:
1. Create S3 Buckets (Source and Destination).
2. Deploy a Lambda function to process files.
3. Set S3 triggers to invoke Lambda.
4. Monitor logs using CloudWatch.

## Lambda Code
The Lambda function code is in `lambda_function.py`.

## IAM Policy
The custom IAM policy can be found in `s3_trigger_policy.json`.
