# Local AI Website Summarizer

A simple AI-powered web application that extracts useful content from a webpage and summarizes it using a locally running LLM through [Ollama](https://ollama.com/).

## Features

- Enter a public website URL
- Automatically adds `https://` when needed
- Removes common noisy HTML elements
- Extracts useful text from headings, paragraphs, list items, and links
- Removes duplicate extracted text
- Detects locally installed Ollama models
- Lets the user choose which local model to use
- Produces the final summary in Markdown
- Runs the LLM locally, so no cloud AI API key is required

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web interface |
| Requests | Fetch webpage HTML |
| BeautifulSoup | Parse and clean HTML |
| Ollama | Run local LLMs |
| OpenAI Python SDK | Communicate with Ollama's OpenAI-compatible API |

## Project Structure

```text
local-ai-website-summarizer/
├── app.py
├── scraper.py
├── summarizer.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

```text
Website URL
    ↓
Requests downloads the HTML
    ↓
BeautifulSoup parses and cleans the page
    ↓
Useful text is extracted and deduplicated
    ↓
Prompt + cleaned website content
    ↓
Selected local Ollama model
    ↓
Markdown summary
    ↓
Streamlit displays the result
```

The summarizer first identifies the main topic or purpose of the webpage. It then prioritizes content related to that topic and de-emphasizes unrelated navigation, footer text, social links, advertisements, sidebars, recommendations, and unrelated sections.

## Requirements

Before running the project, install:

- Python 3.10 or newer
- Ollama
- At least one Ollama model

Python 3.11 or 3.12 is recommended.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/local-ai-website-summarizer.git
cd local-ai-website-summarizer
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install Ollama

Download Ollama from:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

### 3. Download a model

For example:

```bash
ollama pull llama3.2
```

Check the models installed locally:

```bash
ollama list
```

The application automatically detects installed Ollama models and displays them in the model selector.

### 4. Make sure Ollama is running

On Windows and macOS, Ollama usually runs in the background after installation.

If needed, start it manually:

```bash
ollama serve
```

This project expects Ollama at:

```text
http://localhost:11434
```

### 5. Create a virtual environment

#### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 6. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Streamlit will normally open the application automatically. Otherwise, open:

```text
http://localhost:8501
```

## How to Use

1. Make sure Ollama is running.
2. Open the Streamlit app.
3. Enter a website URL.
4. Choose one of your installed Ollama models.
5. Click **Summarize Website**.
6. Wait while the app fetches, cleans, and summarizes the webpage.
7. Read the generated Markdown summary.

Example URL:

```text
https://example.com
```

## Main Components

### `app.py`

Provides the Streamlit interface. It accepts a URL, loads the available local Ollama models, lets the user select a model, and displays the generated summary.

### `scraper.py`

Fetches the webpage with `requests`, parses the HTML with BeautifulSoup, removes common unwanted elements, extracts useful text, and removes duplicates.

### `summarizer.py`

Finds locally installed Ollama models, builds the system and user prompts, sends the cleaned webpage text to the selected model through Ollama's OpenAI-compatible API, and returns the generated summary.

## Notes and Limitations

This is a learning project, not a production-grade web crawler.

Some websites may not work correctly because they:

- rely heavily on JavaScript
- block automated requests
- require authentication
- use anti-bot protection
- have unusual HTML structures

Summary quality and speed depend on the selected Ollama model and your hardware. Larger models may require more RAM or GPU memory.

## Possible Future Improvements

- Support JavaScript-rendered websites
- Add configurable summary length
- Export summaries to files
- Save summary history
- Compare multiple local models
- Add more advanced content extraction
- Add Docker support

## Why I Built This

This project was created as a hands-on exercise to practice:

- web scraping
- HTML parsing and cleaning
- prompt engineering
- local LLM inference
- model selection
- error handling
- Streamlit application development

## License

This project is intended for educational and portfolio purposes.
