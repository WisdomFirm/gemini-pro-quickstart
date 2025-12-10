Gemini Pro Quickstart 🚀

A clean, production-ready Python starter kit to interact with Google's Gemini Pro API. This project demonstrates authentication handling and generative text processing in a modular script.

Developed by WisdomFirm for developers exploring LLM integration.

⚠️ Development Notice (v0.1.0)

This project is currently a pre-release version (v0.1.0). It is designed for educational purposes and rapid prototyping. Production implementation may require additional error handling and security measures.

🚀 Key Features

🔑 Secure Authentication: Uses environment variables to handle API keys securely (no hardcoded secrets).

⚡ Minimalist Architecture: A lightweight script with zero unnecessary dependencies.

📝 Content Generation: Demonstrates how to send prompts and receive text responses from the Gemini model.

🐍 Pythonic Design: Clean, readable code following PEP 8 standards.

🛠️ Prerequisites

Python 3.9 or higher.

A Google Cloud Project with the Gemini API enabled.

An API Key from Google AI Studio.

💻 Installation & Usage

1. Installation

Clone the repository and install the required dependencies:

git clone [https://github.com/WisdomFirm/gemini-pro-quickstart.git](https://github.com/WisdomFirm/gemini-pro-quickstart.git)
cd gemini-pro-quickstart
pip install -r requirements.txt


2. Configuration (API Key)

Set your API key as an environment variable. This is a security best practice.

Linux / macOS:

export GOOGLE_API_KEY="YOUR_API_KEY"


Windows (Command Prompt):

set GOOGLE_API_KEY=YOUR_API_KEY


Windows (PowerShell):

$env:GOOGLE_API_KEY="YOUR_API_KEY"


3. Execution

Run the main script to test the connection:

python main.py


📋 Example Output

When running the script, you should see an output similar to this:

--- Generating content with Gemini Pro --- 

Prompt: Write a short, inspirational quote about learning and technology.

Response:
"Technology is the brush, but learning is the art. Together, they paint a future limited only by our imagination."
------------------------------------------


📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

<p align="center">
Built with ❤️ by <strong>WisdomFirm Team</strong>




<em>Innovating Education & Business through AI Automation.</em>
</p>
