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
   **poetry new project_name**
2. Environment setup
   2.1 Get the path to Python
       **where python**

   2.2 Create a local environment
       **poetry env use C:\Users\max20\AppData\Local\Programs\Python\Python312\python.exe**

   2.3 Activate the local environment (\Scripts\activate)
       **C:\Users\max20\AppData\Local\pypoetry\Cache\virtualenvs\smart-crypto-trader-project-1-FINkROHc-py3.12\Scripts\activate**

   2.4 Check environment dependencies
       **pip freeze**

   2.5 Check the location of the environment
       **where pip**

   2.6 Install packages
       **poetry add package**

   2.7 Install development packages
       **poetry add -D mypy**

   2.8 View package dependency tree
       **poetry show --tree**

## Links

binance-docs:

1. api docs <https://binance-docs.github.io/apidocs/spot/en/#change-log>
2. binance-connector-python <https://github.com/binance/binance-connector-python>
