#### Imp. Note: when you want to deal with sensitive information you will go with environment variables not command line arguments, as in Comm. line arg. someone can see what run command you gave during the process but when you use env variable you don't write passwords etc. on run command and script read the variable itself so security maintained.<br/>
EXample : Comm. line arg. -   python file.py 'password'   <br/>
          Env Var -    python file.py  <br/>

Environment variables are used to manage configuration settings and sensitive information(API key, tokens, passwords, certificates etc.) in a way that is both secure and easily configurable.<br/>
Using environment variables in Python is straightforward and can be done using the `os` module and "python-dotenv" package. <br/>

### Setting Environment Variables

You typically set environment variables in your 'operating system' (directly reading from command line) or via a `.env` file if you are using a package like `python-dotenv`. <br/>
Python-dotenv package reads key-value pairs from a .env file and can set them as environment variables.<br/>

### Accessing Environment Variables in Python

1. **Using `python-dotenv` (optional but useful for development)**:
   - Install `python-dotenv`:
     ```sh
     pip install python-dotenv
     ```

   - Create a `.env` file in your project directory(write your env vars inside it):
     ```env
     MY_VARIABLE=value
     ```

### Example Python Script

Using .env file (for that dotenv package is needed):

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# os.getenv() is used to read the environment variables
my_variable = os.getenv('MY_VARIABLE')  
my_variable_with_default = os.getenv('MY_VARIABLE', 'default_value')

print(f'MY_VARIABLE: {my_variable}')
print(f'MY_VARIABLE with default: {my_variable_with_default}')
```

**Run the script**:
   ```sh
   python your_script.py
   ```

### if not using python-dotenv package means no `.env` file 

1. **Set an environment variable** (optional, if not using `.env` file, you can give env vars before running the script/app on terminal itself ):
   ```sh
   export MY_VARIABLE=hello_world
   ```
you can pass multiple env var in multiple line or all in single line (with space in between) <br/>
example: 
   export VAR1=value1 VAR2=value2 VAR3=value3

2. **Run the script**:
   ```sh
   python your_script.py
   ```


Here's how you set/give environment variables in different operating systems:

#### Windows (Command Prompt)
```sh
set MY_VARIABLE=value
```

#### macOS/Linux (Terminal)
```sh
export MY_VARIABLE=value
```


This will output the value of `MY_VARIABLE`. If the environment variable is not set, it will use the default value provided in the `os.getenv` function.
