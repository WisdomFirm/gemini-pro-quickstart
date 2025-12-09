# Gemini Pro Quickstart 🚀

A simple, clean Python script to get started with Google's Gemini Pro API. This project demonstrates how to connect to the API and generate text based on a prompt.

Developed by [WisdomFirm](https://github.com/WisdomFirm).

## Prerequisites

* Python 3.9 or higher
* A Google Cloud project with the Gemini API enabled
* An API Key for the Gemini API

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/WisdomFirm/gemini-pro-quickstart.git](https://github.com/WisdomFirm/gemini-pro-quickstart.git)
    cd gemini-pro-quickstart
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Set up your API Key:**
    You can set your API key as an environment variable named `GOOGLE_API_KEY`.

    On Linux/macOS:
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY"
    ```

    On Windows (Command Prompt):
    ```cmd
    set GOOGLE_API_KEY=YOUR_API_KEY
    ```

    On Windows (PowerShell):
    ```powershell
    $env:GOOGLE_API_KEY="YOUR_API_KEY"
    ```

2.  **Run the script:**
    ```bash
    python main.py
    ```

## Example Output

```text
--- Generating content with Gemini Pro --- 

Prompt: Write a short, inspirational quote about learning and technology.

Response:
"Technology is the brush, but learning is the art. Together, they paint a future limited only by our imagination."
------------------------------------------
