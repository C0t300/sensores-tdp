# Lambda 1

Lambda 1 is a simple lambda function that receives data from the listener and sends it to the database.

## Requirements

- Python >3.8
- [pg8000](https://github.com/tlocke/pg8000)

## How to use:

Send the http request in a json including the data from the sensors:

```json
{
	"sensor": "humedad",
	"valor": 492,
	"fecha": "2021-05-01 12:00:00"
}
```

You can also include the bool "error" if you want. If not, it is defaulted to false.

## For uploading the package to AWS Lambda

Follow [this link](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html).
