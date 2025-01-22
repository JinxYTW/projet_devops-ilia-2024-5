# Tweet Microservice Documentation

## Production Deployment

@TODO

## Developer Guide

### Prerequisites

- Docker
- Python
- WSL (for Windows users)

### Workflows

#### Commit

To make commits, you should use

#### Versionning

To version our project, we'll use the python library [semantic-release](https://github.com/semantic-release/semantic-release)

#### Test-Driven Development (TDD)

1. **Write a Test**: Start by writing a test for the new functionality. This test should fail initially since the functionality is not yet implemented.

2. **Run the Test**: Execute the test to ensure it fails. This step confirms that the test is correctly identifying the absence of the desired functionality.

3. **Write the Code**: Implement the minimum amount of code required to make the test pass. Focus on getting the test to pass, not on writing perfect code.

4. **Run the Test Again**: Execute the test again to verify that it now passes with the new code in place.

5. **Refactor**: Refactor the code to improve its structure and readability while ensuring that the test still passes. This step helps in maintaining clean and maintainable code.

6. **Repeat**: Continue this cycle for each new piece of functionality.


#### Automated

To automate the testing and linting process, we will use GitHub Actions. This workflow will trigger on every push and pull request to the `main` branch, check out the code, set up Python, install dependencies, run linters, and execute tests.

### Project Architecture

The Tweet Microservice is structured as follows:

```
/tweet-microservice
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   └── services.py
├── tests
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_models.py
│   └── test_services.py
├── data
│   └── sample_data.json
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

This structure ensures a clear separation of concerns, making the codebase maintainable and scalable.

## Launching Swagger

To start the API documentation, run `make swagger` in a terminal or execute the corresponding command from the Makefile.
You should have wsl launched for this to work.

## Error Handling

### Docker x Swagger
If you see the pet store when you launch the swagger, it means that the swagger is not able to find the correct yaml file.
That is because docker is not able to find the correct path to the yaml file and then create a directory with the name of this yaml file.
Only because when you are on windows, the path is different from the one that docker is expecting.

> To fix this, you need to go into the *makefile* directory and then start wsl and run the command `make swagger` again.
> You should be able to see the correct swagger documentation now.

