#!/usr/bin/env bash
S3ProcessedDataOutputBucket=arc301-serverless-output
NotificationEmailAddress=akhtarh@amazon.com
AnomalyThresholdScore=1
LamdaCodeUriBucket=arc301-serverless-lamdacode
REGION=ap-southeast-1

FILE="$(uuidgen).yaml"
cd /home/ec2-user/arc301-deploy

aws cloudformation package --region $REGION --template-file SAM-For-RealTimeAnalytics.yaml --s3-bucket $LamdaCodeUriBucket --output-template-file $FILE
aws cloudformation deploy --region $REGION --template-file $FILE --stack-name DeviceDataRealTimeAnalyticsStack --parameter-overrides "ProcessedDataBucketName=$S3ProcessedDataOutputBucket" "NotificationEmailAddress=$NotificationEmailAddress" "AnomalyThresholdScore=$AnomalyThresholdScore" "LamdaCodeUriBucket=$LamdaCodeUriBucket"  --capabilities CAPABILITY_NAMED_IAM
