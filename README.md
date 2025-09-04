# Advanced AI Research Agent 

A comprehensive, feature-rich research agent powered by Claude 3.5 Sonnet with multiple search capabilities, intelligent caching, and beautiful rich formatting.

## ✨ Features

### 🔍 Multiple Research Sources
- **Wikipedia Search** - General knowledge and encyclopedia entries
- **Web Search** - Current information and trending topics via DuckDuckGo
- **News Search** - Latest developments from major news sources
- **Academic Papers** - Research papers from arXiv
- **Web Content Extraction** - Extract content from specific URLs

### 🎯 Smart Research Templates
- **Technology Research** - Tech topics, innovations, and trends
- **Business Analysis** - Market research and company analysis
- **Academic Research** - Scholarly topics and literature review
- **Health & Medicine** - Medical topics and wellness information
- **Historical Research** - Historical events, periods, and figures
- **Comparative Analysis** - Compare and contrast different options

### 💾 Advanced Export Options
- **JSON Format** - Structured data for developers
- **Text Format** - Human-readable reports
- **PDF Format** - Professional documents with formatting
- **All Formats** - Export to all formats simultaneously
- **Auto-save** - Automatic saving in your preferred format

### ⚙️ Configuration & Performance
- **Intelligent Caching** - Faster repeated queries with 24-hour cache
- **Rich UI** - Beautiful terminal interface with colors and formatting
- **Progress Bars** - Visual feedback during research operations
- **Verbose Mode** - Detailed debugging information
- **Customizable Settings** - Adjust behavior to your preferences

### 🎮 User Experience
- **Interactive Menus** - Easy-to-navigate interface
- **Template-Based Research** - Guided research with predefined questions
- **Cache Management** - View statistics and clear expired cache
- **Help System** - Built-in documentation and usage tips
- **Error Recovery** - Robust error handling with fallback options

## 📋 Prerequisites

- **Python 3.13** or higher (tested with Python 3.13)
- **Anthropic API Key** - Get one from [Anthropic's Console](https://console.anthropic.com/)
- **Internet Connection** - Required for web search and API calls

## 🚀 Quick Setup

1. **Clone or download this project**

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
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

6. **Run the research agent**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
research-agent/
├── main.py              # Main application with enhanced UI
├── tools.py             # Research tools and web search capabilities
├── config.py            # Configuration management system
├── cache.py             # Intelligent caching system
├── templates.py         # Research templates for different domains
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── research_outputs/   # Directory for saved research results
├── .cache/             # Cache directory for faster queries
└── venv/               # Virtual environment
```

## 🎯 Usage Examples

### Custom Research Query
```
🔍 Custom Research Query
Enter your research question: How does quantum computing work and what are its applications?
```

### Template-Based Research
```
🎯 Template-Based Research
Select a template:
1. Technology Research
2. Business Analysis
3. Academic Research

Using Technology template for: blockchain
Generated Research Questions:
1. What is blockchain and how does it work?
2. What are the latest developments in blockchain?
3. What are the advantages and disadvantages of blockchain?
```

### Settings Configuration
```
⚙️ Settings & Configuration
Current Settings:
- Caching: ✅ Enabled
- Auto Save: ✅ Enabled
- Rich Formatting: ✅ Enabled
- Default Format: JSON
```

## 🔧 Dependencies

### Core Framework
- **langchain** - LangChain framework for AI applications
- **langchain-anthropic** - Anthropic Claude integration
- **langchain-community** - Community tools and utilities
- **langchain-openai** - OpenAI integration (available)

### Research Tools
- **wikipedia** - Wikipedia API access
- **duckduckgo-search** - Web search capabilities
- **arxiv** - Academic paper search
- **requests** - HTTP requests for web content
- **beautifulsoup4** - HTML parsing and content extraction

### User Interface
- **rich** - Beautiful terminal formatting and progress bars
- **colorama** - Cross-platform colored terminal text

### Document Generation
- **reportlab** - PDF generation and formatting
- **tqdm** - Progress bars and status indicators

### Utilities
- **python-dotenv** - Environment variable management
- **pydantic** - Data validation and parsing
- **lxml** - XML and HTML processing

## ⚙️ Configuration Options

The research agent automatically creates an `agent_config.json` file with these settings:

```json
{
  "model_name": "claude-3-5-sonnet-20240620",
  "temperature": 0.1,
  "max_search_results": 8,
  "enable_caching": true,
  "cache_duration_hours": 24,
  "use_rich_formatting": true,
  "auto_save": false,
  "default_format": "json",
  "output_directory": "research_outputs"
}
```

## 🎨 Rich UI Features

- **🎨 Colored Output** - Beautiful syntax highlighting and formatting
- **📊 Tables** - Organized display of results and statistics  
- **📋 Panels** - Grouped information with borders and titles
- **⏳ Progress Bars** - Visual feedback during operations
- **✅ Status Icons** - Clear success/error indicators
- **🎯 Interactive Prompts** - Smart input validation and suggestions

## 📊 Cache Management

- **Automatic Caching** - Results cached for 24 hours by default
- **Cache Statistics** - View total files, size, and validity
- **Expired Cleanup** - Automatic removal of old cache files
- **Manual Control** - Clear cache or disable caching entirely

## 🔍 Research Templates

Each template provides structured research with predefined questions:

- **Technology**: Technical definition, applications, trends, challenges
- **Business**: Market analysis, competitors, trends, opportunities
- **Academic**: Literature review, methodologies, recent findings
- **Health**: Causes, symptoms, treatments, prevention
- **Historical**: Timeline, context, figures, consequences
- **Comparative**: Differences, similarities, use cases, recommendations

## 🐛 Troubleshooting

### Common Issues

**API Key Problems**
- Ensure `.env` file exists with valid `ANTHROPIC_API_KEY`
- Check API key has sufficient credits
- Verify no extra spaces in the key

**Import Errors**
- Activate virtual environment: `venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.13+)

**Search Failures**
- Check internet connection
- Try disabling cache in settings
- Enable verbose mode for debugging

**PDF Generation Issues**
- Ensure reportlab is installed
- Check file permissions in output directory
- Falls back to text format automatically

### Debug Mode

Enable verbose mode in settings to see detailed debugging information:
- API request/response details
- Tool execution logs
- Cache hit/miss information
- Error stack traces

## 🚀 Performance Tips

1. **Enable Caching** - Significantly speeds up repeated queries
2. **Use Templates** - More focused and efficient research
3. **Adjust Cache Duration** - Longer for stable topics, shorter for news
4. **Auto-save Results** - Avoid manual export steps
5. **Rich Formatting** - Better visualization of complex data

## 📝 License

This project is for demonstration and educational purposes. Feel free to modify and extend for your research needs.

## 🤝 Contributing

Suggestions and improvements welcome! Areas for enhancement:
- Additional research sources
- New template types
- Export format options
- UI/UX improvements
- Performance optimizations

---

**Happy Researching!** 🔬✨
