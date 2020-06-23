# cicd-tutorial
CI/CD code used within the AnitaB.org demo to make a executable, serverless function within AWS (Lambda Function))

testspec.yml is used to allow AWS CodeBuild to execute the tests in lambdaFunction/test/test_lambdaFunction.py

buildspec.yml is used to allow AWS CodeBuild to execute commands that will package the code into an executable lambda function.
This file references template.yml, which is used by buildspec.yml to describe how the function is built.

template.yml is used to describe the requirements and stucture of the lambda function.
This file points to file locations of code being used, and descibes which language is used to execute the function.
