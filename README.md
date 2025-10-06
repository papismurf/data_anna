# Data Anna

A Python-based financial data analysis tool that fetches and analyzes S&P 500 stock data.

## Overview

Data Anna is a streamlined application designed to retrieve and process financial data from the S&P 500 index. The project leverages popular financial analysis libraries to provide insights into market data.

## Features

- **S&P 500 Data Retrieval**: Automatically fetches the current list of S&P 500 companies from Wikipedia
- **Stock Information**: Retrieves ticker symbols and company names for all S&P 500 constituents
- **Technical Analysis Ready**: Integrated with TA-Lib for technical indicators
- **Real-time Data**: Uses yfinance for accessing up-to-date stock market data
- **Web Interface**: Built with Streamlit for interactive data visualization (coming soon)

## Prerequisites

- Python 3.13 or higher
- uv package manager (or pip)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-anna.git
cd data-anna
```

2. Install dependencies using uv:
```bash
uv install
```

Or with pip:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script to fetch S&P 500 tickers:

```bash
python main.py
```

## Dependencies

- **pandas** (>=2.3.3): Data manipulation and analysis
- **streamlit** (>=1.50.0): Web application framework
- **ta-lib** (>=0.6.7): Technical analysis library
- **yfinance** (>=0.2.66): Yahoo Finance market data downloader

## Project Structure

```
data-anna/
├── main.py          # Main application entry point
├── tests/           # Test directory
├── pyproject.toml   # Project configuration and dependencies
├── uv.lock          # Dependency lock file
├── README.md        # This file
└── .gitignore       # Git ignore rules
```

## Development

This project uses:
- PyCharm as the IDE (see `.idea/` configuration)
- Git for version control
- uv for dependency management

## Future Enhancements

- Implement Streamlit web interface for data visualization
- Add technical indicators using TA-Lib
- Include real-time stock data fetching with yfinance
- Create data analysis and visualization features

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]