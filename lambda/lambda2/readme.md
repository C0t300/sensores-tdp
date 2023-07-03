# Lambda 2

Lambda 2 is a simple lambda function that receives data from the listener and sends it to the database.

## Requirements

- Python >3.8
- [pg8000](https://github.com/tlocke/pg8000)

## How to use:

Send the http request in a json including the sensor that you want the data from:

```json
{
	"sensor": "humedad"
}
```

## For uploading the package to AWS Lambda

Follow [this link](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).
