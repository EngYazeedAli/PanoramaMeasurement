# FastAPI Backend Royal Commission Challenge Project

## Overview

This is a FastAPI project of the use case used in the Evaluation Challenge is for a small Employee Attendance System Web Application
which contains the basic functionality of any project such as creating, updating, and deleting records

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Dependencies](#dependencies)
- [Permission](#permission)

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/your-username/fastapi-project.git](https://github.com/EngYazeedAli/fastapi_royal_test.git)
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-project
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   The `--reload` option enables auto-reloading on code changes during development.

2. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the Swagger documentation.

3. Explore and interact with the API using the provided endpoints.


## Project Structure

- `app/main.py`: FastAPI application creation and main endpoint routing.
- `app/api/`: Directory for endpoint routers.
-  `services/`: Directory for business logic services.
- `app/models/`: Directory for Pydantic models.
- `config/`: Directory for configuration files.
- `requirements.txt`: Project dependencies.

## Configuration

- Update the configuration settings in `app/main.py` and other relevant files based on your project requirements.

## API Documentation

The API documentation is automatically generated using FastAPI's built-in Swagger UI. Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore and interact with the API.

## Dependencies

List of major dependencies used in this project:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

For a complete list, check the `requirements.txt` file.


## Permission

To access and test the project, please use the following admin log-in details:
- Username: admin@system.com.
- Password: admin@0548.
