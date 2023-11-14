# Web application for identifying completed forms
This app implements tree menu using a template tag

## Getting started
These instructions will help you set up and run the project on your local machine.

### Prerequisites

- python 3.x
- pip
- Git
- Virtual Environment (recommended)

### Installation

1. Clone this repository to your local machine using the following command:

    ```bash
   git clone https://github.com/hamidullaorifov/eKomTask.git
   ```

2. Navigate to the project directory:

    ```bash
   cd eKomTask
   ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

- On Windows
    ```bash
    venv\Scripts\activate
    ```
- On macOS and Linux
    ```bash
    source venv/bin/activate
    ```
5. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run test cases
    ```bash
    python manage.py test api
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```
8. Send requests to http://localhost:8000/get_form/ .







