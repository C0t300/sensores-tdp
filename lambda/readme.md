# AWS Lambda Functions

This is fun but not at 2 am.

## Explanations

### Lambda 1

Lambda 1 does the insert into the database. It receives the data from the listener and sends it to the database.

### Lambda 2

Lambda 2 does the query to the database. It may be used to create some kind of dashboard.

## ToDo:

- Probably do a proper authentication system in both lambda functions, as if anyone knows the url they can **send many requests and give all our money to Jeff Bezos**.
