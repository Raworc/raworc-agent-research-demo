# LangChain Claude Demo

A simple Python project demonstrating how to use LangChain with Anthropic's Claude AI model to answer questions.

## Description

This project sets up a basic interaction with Claude 3.5 Sonnet using the LangChain framework. It loads environment variables, initializes the Claude model, and demonstrates a simple query-response interaction.

## Prerequisites

- Python 3.7 or higher
- An Anthropic API key

## Setup

1. **Clone or download this project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add your Anthropic API key:
     ```
     ANTHROPIC_API_KEY=your_api_key_here
     ```
   - You can get an API key from [Anthropic's Console](https://console.anthropic.com/)

## Running the Project

With your virtual environment activated and dependencies installed:

```bash
python main.py
```

This will run the demo script that asks Claude "What is the capital of France?" and prints the response.

## Project Structure

```
├── main.py              # Main script with Claude interaction
├── tools.py             # Currently empty, for future tool implementations
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this file)
├── .gitignore          # Git ignore rules
└── venv/               # Virtual environment (created after setup)
```

## Dependencies

- **langchain**: Core LangChain framework
- **langchain-anthropic**: Anthropic integration for LangChain
- **langchain-openai**: OpenAI integration (available but not used)
- **langchain-community**: Community tools and integrations
- **python-dotenv**: Environment variable loading
- **pydantic**: Data validation
- **wikipedia**: Wikipedia API access

## Customization

You can modify `main.py` to:
- Change the question being asked
- Adjust the model temperature
- Switch to a different Claude model
- Add more complex interactions

## Troubleshooting

- **API Key Issues**: Make sure your `.env` file contains a valid `ANTHROPIC_API_KEY`
- **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **Virtual Environment**: Make sure your virtual environment is activated before running the script

## License

This project is for demonstration purposes.
