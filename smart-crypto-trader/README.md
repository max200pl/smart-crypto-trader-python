# Project Name

A brief description of your project.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Formatter](#formatter)
  - [Installation](#installation)
  - [Links](#links)

## Formatter

1. Link: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>
2. added into Settings Json

    ```json
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    }
    ```

## Installation

Explain how to install and set up your project.
Poetry <https://python-poetry.org/>

1. Project creation
   1. **poetry new --src my-package**
   2. activates the virtual environment. **poetry shell**

2. Environment setup
   1. Get the path to Python **where python**
   2. Info about environment **poetry env info**
   3. Create a local environment **poetry env use C:\Users\max20\AppData\Local\Programs\Python\Python312\python.exe**
   4. Activate the local environment (\Scripts\activate)  **poetry C:\Users\max20\AppData\Local\pypoetry\Cache\virtualenvs\smart-crypto-trader\Scripts\activate**
   5. Check environment dependencies **pip freeze**
   6. Check the location of the environment **where pip**
   7. Install packages **poetry add package**
   8. Install development packages **poetry add -D mypy**
   9. View package dependency tree **poetry show --tree**

## Links

binance-docs:

1. api docs <https://binance-docs.github.io/apidocs/spot/en/#change-log>
2. binance-connector-python <https://github.com/binance/binance-connector-python>
