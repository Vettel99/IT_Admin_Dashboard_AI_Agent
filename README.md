# Decawork IT Support Agent

An AI agent designed to execute natural-language IT support requests (like creating users and resetting passwords) by interacting with a web-based admin panel. 

This project was built for the Decawork AI Engineering Internship assessment.

## Architecture & Tooling

* **Mock IT Admin Panel:** Built with `FastAPI` and pure HTML forms. It acts as a lightweight, functional target for the agent to navigate.
* **AI Agent:** Built using the `browser-use-sdk`.
* **LLM Engine:** The agent relies on Browser Use's Cloud SDK. Under the hood, this utilizes their ChatBrowserUse dynamic routing engine, which automatically delegates the DOM parsing and execution steps to the most capable frontier foundation model available.
* **Conditional Routing:** Complex, multi-step instructions (e.g., checking if a user exists before creating them) are handled naturally through the agent's prompt context rather than brittle, hard-coded `if/else` DOM selectors.

## Prerequisites

1.  Python 3.10+
2.  A valid Browser Use API Key.
3.  [Ngrok](https://ngrok.com/) (to expose the local FastAPI server to the cloud-based agent).

## Setup Instructions

### 1. Create a Virtual Environment

It is highly recommended to use a virtual environment to isolate project dependencies. 

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

Clone the repository and install the required Python packages:
```bash
git clone <your-repo-url>
cd decawork-it-agent
pip install -r requirements.txt
```

### 3. Configure Environment

Create a .env file in the root directory and add your API key:
```bash
BROWSER_USE_API_KEY=your_actual_api_key_here
```

### 4. Start the Mock Admin Panel

Launch the FastAPI server locally:

```bash
python app.py
```

The server will start at http://localhost:8000.

### 5. Install and Expose the Server via Ngrok
Because the cloud-based agent needs a public URL to navigate to your local site, you must expose your local port 8000 using Ngrok.

**A. Install Ngrok**
* **macOS:**
    Use Homebrew to install Ngrok:
    ```bash
    brew install ngrok/ngrok/ngrok
    ```
* **Windows:**
    Download the `.zip` file from the [Ngrok website](https://ngrok.com/download) and extract the executable, or install it via Chocolatey:
    ```cmd
    choco install ngrok
    ```

**B. Authenticate (First-time only)**
If you haven't used Ngrok before, create a free account at [ngrok.com](https://ngrok.com/), copy your authentication token from the dashboard, and run:
```bash
ngrok config add-authtoken <YOUR_AUTH_TOKEN>
```
**C. Start the Tunnel**
In a new terminal window, start the tunnel to your running FastAPI server:

```bash
ngrok http 8000
```
(Copy the generated https://... forwarding URL from the Ngrok terminal dashboard and paste it into the TARGET_URL variable inside agent.py)


### 6. Run the Agent

Open agent.py and replace the TARGET_URL variable with your generated Ngrok URL. Then, execute the agent in a new terminal window within the virtual environment:

```bash
python agent.py
```

Watch the terminal for the agent's reasoning steps and execution output.

### Loom Walkthrough

https://www.loom.com/share/c259ed77c3bd4a22be0a265df9c34770
