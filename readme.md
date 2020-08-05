```
docker build -t lambda-test .
docker run -v "$PWD":/var/task lambda-test
docker run -e TEST=True -v "$PWD":/var/task lambci/lambda:python3.6 lambda_function.lambda_handler
```
