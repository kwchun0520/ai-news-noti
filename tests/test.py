import boto3

client = boto3.client("lambda")

response = client.invoke(
    FunctionName='ai-news-noti',
    InvocationType='RequestResponse',
    LogType='Tail',
    Payload='{}'
)

print(response)