# midterm_calculator
**Documentation for Design Patterns Implementation**

### Strategy Pattern

**Description:** The Strategy Pattern is implemented in our calculator application to encapsulate each arithmetic operation (addition, subtraction, multiplication, division) into separate strategy classes. This allows us to easily switch between different strategies at runtime, making the application more flexible and scalable.

**Link to Implementation:** [Strategy Pattern Implementation](https://github.com/your_username/calculator_app/strategy_pattern.py)

**Short Description:** The Strategy Pattern involves defining a family of algorithms, encapsulating each one into separate classes, and making them interchangeable. In our calculator application, we have strategy classes for addition, subtraction, multiplication, and division, each implementing a `calculate` method.

### Singleton Pattern

**Description:** The Singleton Pattern ensures that a class has only one instance and provides a global point of access to that instance. In our application, the Calculator class is implemented as a singleton to ensure that only one calculator instance exists throughout the application.

**Link to Implementation:** [Singleton Pattern Implementation](https://github.com/your_username/calculator_app/singleton.py)

**Short Description:** The Singleton Pattern involves defining a class that can only be instantiated once and providing a static method to access the instance. In our application, the Calculator class is implemented as a singleton to ensure that all calculations are performed using the same calculator instance.

### Factory Method Pattern

**Description:** The Factory Method Pattern is used to define an interface for creating an object, but allow subclasses to alter the type of objects that will be created. In our application, we have a Factory class that creates instances of different arithmetic operation strategies based on user input.

**Link to Implementation:** [Factory Method Pattern Implementation](https://github.com/your_username/calculator_app/factory_method.py)

**Short Description:** The Factory Method Pattern involves defining an interface for creating objects and letting subclasses decide which class to instantiate. In our application, the Factory class creates instances of strategy classes based on user input, allowing for dynamic object creation.

---

**Configuration Examples and Environment Variables Usage**

### Environment Variables Usage

**Description:** Environment variables are used in our calculator application to configure settings such as file paths, API keys, and other sensitive information. This allows us to separate configuration from code and makes it easier to deploy the application across different environments without hardcoding values.

**Link to Code:** [Environment Variables Usage](https://github.com/your_username/calculator_app/config.py)

**Short Description:** We define environment variables in a separate configuration file (`config.py`) and access them using the `os.environ` dictionary. This ensures that sensitive information is not hard-coded into the application and can be easily changed without modifying the code.

**Configuration Examples:** Below is an example of how environment variables are defined in the `config.py` file:

```python
import os

# Database Configuration
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')

# API Keys
API_KEY = os.environ.get('API_KEY')
```

---

**Logging Implementation and Usage**

### Logging Implementation

**Description:** Logging is implemented in our calculator application to record important events, errors, and debugging information. This helps us monitor the application's behavior, troubleshoot issues, and analyze performance.

**Link to Code:** [Logging Implementation](https://github.com/your_username/calculator_app/logger.py)

**Short Description:** We use Python's built-in logging module to implement logging in our application. We configure different loggers, handlers, and formatters to customize the logging behavior according to our requirements.

**Usage Example:** Below is an example of how logging is used in our application to record an error:

```python
import logging

# Create a logger
logger = logging.getLogger(__name__)

try:
    # Perform some operation
    result = perform_operation()
except Exception as e:
    # Log the error
    logger.error(f"An error occurred: {e}")
```

---

**Exception Handling: Look Before You Leap (LBYL) vs. Easier to Ask for Forgiveness than Permission (EAFP)**

### Look Before You Leap (LBYL)

**Description:** Look Before You Leap (LBYL) is a programming style that checks for preconditions before performing an operation to avoid potential errors or exceptions. In our calculator application, we use LBYL to validate user input before performing arithmetic operations.

**Link to Code:** [LBYL Implementation](https://github.com/your_username/calculator_app/lbyl_example.py)

**Short Description:** We check for conditions such as division by zero or invalid input before performing arithmetic operations. This helps prevent runtime errors and ensures the stability of the application.

### Easier to Ask for Forgiveness than Permission (EAFP)

**Description:** Easier to Ask for Forgiveness than Permission (EAFP) is a programming style that assumes the validity of an operation and handles any potential errors or exceptions that may occur. In our calculator application, we use EAFP to catch and handle exceptions that may arise during arithmetic operations.

**Link to Code:** [EAFP Implementation](https://github.com/your_username/calculator_app/eafp_example.py)

**Short Description:** We perform arithmetic operations without explicitly checking for preconditions. Instead, we use try-except blocks to catch and handle any exceptions that may occur during the execution of the operation. This allows for cleaner and more concise code, focusing on handling exceptions rather than checking preconditions.

---


##Working Video demonstration:


## Video Demonstration

Watch the video demonstration of our calculator application:

[![Calculator Video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://app.vidcast.io/share/76a1459d-1b0b-48f2-b2e0-7f0a02afef23)




## Calculator Application Setup and Usage Instructions

### 1. Installation

#### Prerequisites
- Python 3.x installed on your system ([Download Python](https://www.python.org/downloads/))
- pip package manager installed with Python

#### Setup Steps
1. Clone or download the calculator application from the repository.

   ```bash
   git clone <repository-url>
   cd calculator-application
   ```

2. Set up a virtual environment (optional but recommended).
   
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment.

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Unix/Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies from the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

### 2. Configuration

- If your application requires any configuration settings, provide instructions on how to set them up. For example, if you are using environment variables, explain how to create a `.env` file and specify the required variables.

### 3. Usage

1. Run the main script of the calculator application.

   ```bash
   python main.py
   ```

2. Follow the prompts or instructions provided by the application to perform calculations.

### 4. Features

- Describe the main features of the calculator application.
- Provide examples of common use cases.

### 5. Additional Information

- Troubleshooting tips
- Contact information for support or feedback

### Example Use Case

Suppose you want to calculate the sum of two numbers:

1. Run the calculator application.
   
   ```bash
   python main.py
   ```

2. Choose the addition operation from the menu.

3. Enter the first number when prompted.

4. Enter the second number when prompted.

5. The application will display the result of the addition operation.


