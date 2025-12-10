# Gemini Pro Quickstart 🚀

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
![Status](https://img.shields.io/badge/status-pre--release-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A clean, production-ready **Python starter kit** to interact with Google's **Gemini Pro API**. This project demonstrates authentication handling and generative text processing in a modular script.

Developed by [WisdomFirm](https://github.com/WisdomFirm) for developers exploring LLM integration.

 ## ⚠️ Development Notice (v0.1.0)
This project is currently a **pre-release** version (`v0.1.0`). It is designed for **educational purposes** and rapid prototyping. Production implementation may require additional error handling and security measures.

 

## Prerequisites

* Python 3.9 or higher
* A Google Cloud project with the Gemini API enabled
* An API Key for the Gemini API

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/WisdomFirm/gemini-pro-quickstart.git](https://github.com/WisdomFirm/gemini-pro-quickstart.git)
    cd gemini-pro-quickstart
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Set up your API Key:**
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

2.  **Run the script:**
    ```bash
    python main.py
    ```

## Example Output

```text
--- Generating content with Gemini Pro --- 

Prompt: Write a short, inspirational quote about learning and technology.
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

Response:
"Technology is the brush, but learning is the art. Together, they paint a future limited only by our imagination."
------------------------------------------
