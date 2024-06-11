# Setting Up Virtual Environment

## Prerequisites

- Python 3 installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).

## Steps

1. Open a terminal or command prompt.

2. Navigate to the root directory of this project in your terminal. In this case, that would be team_hedgecode/backend

3. Run the following command to create a virtual environment named `.venv`:

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    - **On macOS and Linux:**

        ```bash
        source .venv/bin/activate
        ```

    - **On Windows (cmd.exe):**

        ```bash
        .venv\Scripts\activate.bat
        ```

    - **On Windows (PowerShell):**

        ```bash
        .venv\Scripts\Activate.ps1
        ```

5. Run the following command in your terminal or command line to exit the virtual environment:

    ```bash
    deactivate
    ```

## Installing Dependencies

Once the virtual environment is activated, you can install the required dependencies using the `pip` package manager.

1. Make sure your virtual environment is activated.

2. Run the following command to install dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Creating or Updating `requirements.txt`

If you need to update the list of dependencies or create a `requirements.txt` file for a new project, you can use `pip` to generate it.

1. Make sure your virtual environment is activated.

2. Run the following command to generate `requirements.txt`:

    ```bash
    pip freeze > requirements.txt
    ```

This command will capture all installed packages and their versions into `requirements.txt` .
