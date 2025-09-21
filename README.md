# Brochure Gen OpenAI

A Python application that automatically generates company brochures by analyzing websites using OpenAI's GPT models. The application scrapes a company's website, identifies relevant pages, and creates a professional markdown brochure with company information, culture, and career details.

## Features

- **Website Analysis**: Automatically scrapes and analyzes company websites
- **Intelligent Link Selection**: Uses AI to identify the most relevant pages (About, Careers, etc.)
- **Rich Markdown Output**: Generates beautifully formatted brochures in markdown
- **Streaming Interface**: Real-time brochure generation with live updates
- **Console Display**: Rich terminal output with proper markdown rendering

## Prerequisites

- Python 3.13+
- OpenAI API key
- Anaconda/Miniconda (recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dudaka/brochure-gen-openai.git
cd brochure-gen-openai
```

2. Create and activate the conda environment:

```bash
conda env create -f environment.yml
conda activate brochure-gen-openai
```

3. Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

Run the application with a company name and website URL:

```python
from src.main import create_brochure, stream_brochure

# Generate a complete brochure
create_brochure('Company Name', 'https://company-website.com')

# Stream brochure generation with live updates
stream_brochure('Company Name', 'https://company-website.com')
```

### Example

The current example generates a brochure for Hugging Face:

```bash
python src/main.py
```

## Project Structure

```
brochure-gen-openai/
├── environment.yml          # Conda environment configuration
├── README.md               # Project documentation
├── src/
│   ├── main.py            # Main application logic
│   ├── website.py         # Website scraping and analysis
│   └── __pycache__/       # Python cache files
└── .env                   # Environment variables (create this)
```

## How It Works

1. **Website Scraping**: The `Website` class extracts content, title, and links from the target website
2. **Link Analysis**: GPT-4o-mini analyzes extracted links to identify relevant pages (About, Careers, etc.)
3. **Content Aggregation**: Relevant pages are scraped and combined into a comprehensive dataset
4. **Brochure Generation**: GPT-4o-mini processes the aggregated content to create a professional brochure
5. **Rich Display**: The brochure is displayed in the terminal with proper markdown formatting using the Rich library

## Key Dependencies

- **OpenAI**: GPT model integration for content analysis and generation
- **Beautiful Soup**: HTML parsing and web scraping
- **Rich**: Enhanced terminal output with markdown rendering
- **Requests**: HTTP requests for website access
- **Python-dotenv**: Environment variable management

## Configuration

The application uses GPT-4o-mini by default. You can modify the model in `src/main.py`:

```python
MODEL = 'gpt-4o-mini'  # Change to your preferred model
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Notes

- Ensure you have sufficient OpenAI API credits before running the application
- The application respects website robots.txt and rate limits
- Generated brochures are displayed in the terminal and not saved to file by default
- Content length is limited to 20,000 characters to stay within API limits
