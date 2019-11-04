from __future__ import print_function
import boto3
import base64

client = boto3.client('sns')
# Include your SNS topic ARN here.
topic_arn = 'arn:aws:sns:us-west-2:700067554982:publishtophone'


def KinesisAnalyticOutputToSNS_handler(event, context):
    output = []
    success = 0
    failure = 0
    
    #print('Begin Processing KA data. Number of records found = (0)' .format(event['records'].count))
    print('Begin Processing KA data. Number of records found')
    for record in event['records']:
        try:
            # Uncomment the below line to publish the decoded data to the SNS topic.
            payload = base64.b64decode(record['data'])
            client.publish(TopicArn=topic_arn, Message=payload, Subject='Sent from Kinesis Analytics')
            output.append({'recordId': record['recordId'], 'result': 'Ok'})
            success += 1
        except ValueError, Argument:
            print('Failed to Process Record = {0}, Exception : ' .format(success, Argument))
            output.append({'recordId': record['recordId'], 'result': 'DeliveryFailed'})
            failure += 1

    print('Successfully delivered {0} records, failed to deliver {1} records'.format(success, failure))
    return {'records': output}
