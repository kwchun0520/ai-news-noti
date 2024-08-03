#usr/zsh
aws lambda invoke --function-name $1 \
    --cli-binary-format raw-in-base64-out \
    --payload '{ "key": "value" }' response.json