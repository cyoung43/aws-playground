# Playground

1. s3 bucket that can ingest files.
2. S3 trigger that will invoke lambda to process file and get file metadata
3. Part two of lambda function will post tweet with file info

## References

<https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference/post-tweets>

Jk likely can't use the Twitter API due to new restriction features... Instead, just use the lambda function to write to a file in s3??

## Next Steps

1. Get metadata from files
2. Write metadata to dynamodb record
3. Hit an API to get data (may be overkill). Otherwise just get data from dynamodb using SDK
