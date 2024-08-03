#usr/zsh
echo $(cat .env| xargs)
REGION=us-east-1

aws events put-rule \
--name my-schedule-rule-for-$1 \
--schedule-expression 'cron(0 13 * * ? *)'


aws lambda add-permission \
--function-name $1 \
--statement-id my-scheduled-event \
--action 'lambda:InvokeFunction' \
--principal events.amazonaws.com \
--source-arn arn:aws:events:$REGION:$AWS_ACCOUNT_ID:rule/my-schedule-rule-for-$1


json='[{"Id":"1","Arn":"arn:aws:lambda:'$REGION':'$AWS_ACCOUNT_ID':function:'$1'"}]'
echo "$json" > targets.json

aws events put-targets --rule my-schedule-rule-for-$1 --targets file://targets.json