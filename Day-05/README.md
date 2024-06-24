Using environment variables in Python is straightforward and can be done using the `os` module. Here's a short and easy guide to work with environment variables:

### Setting Environment Variables

You typically set environment variables in your operating system or via a `.env` file if you are using a library like `python-dotenv`. Here's how you set environment variables in different operating systems:

#### Windows (Command Prompt)
```sh
set MY_VARIABLE=value
```

#### macOS/Linux (Terminal)
```sh
export MY_VARIABLE=value
```

### Accessing Environment Variables in Python

1. **Using the `os` module**:
   ```python
   import os

   # Get the value of the environment variable
   my_variable = os.getenv('MY_VARIABLE')

   # Default value if the environment variable is not set
   my_variable_with_default = os.getenv('MY_VARIABLE', 'default_value')

   print(f'MY_VARIABLE: {my_variable}')
   print(f'MY_VARIABLE with default: {my_variable_with_default}')
   ```

2. **Using `python-dotenv` (optional but useful for development)**:
   - Install `python-dotenv`:
     ```sh
     pip install python-dotenv
     ```

   - Create a `.env` file in your project directory:
     ```env
     MY_VARIABLE=value
     ```

   - Load and access the variables:
     ```python
     from dotenv import load_dotenv
     import os

     # Load environment variables from .env file
     load_dotenv()

     # Get the value of the environment variable
     my_variable = os.getenv('MY_VARIABLE')

     print(f'MY_VARIABLE: {my_variable}')
     ```

### Example Script

Here's a complete example demonstrating both methods:

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Get environment variables
my_variable = os.getenv('MY_VARIABLE')
my_variable_with_default = os.getenv('MY_VARIABLE', 'default_value')

print(f'MY_VARIABLE: {my_variable}')
print(f'MY_VARIABLE with default: {my_variable_with_default}')
```

### Running the Script

1. **Set an environment variable** (optional, if not using `.env` file):
   ```sh
   export MY_VARIABLE=hello_world
   ```

2. **Run the script**:
   ```sh
   python your_script.py
   ```

This will output the value of `MY_VARIABLE`. If the environment variable is not set, it will use the default value provided in the `os.getenv` function.