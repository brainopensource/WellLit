# WellLit – Upstream Well Decline Analysis

**WellLit** is a lightweight Streamlit-based web app for analyzing oil & gas production decline curves.  
It provides interactive visualizations, filtering, and adjustment of well production trends.

## Features

- Interactive decline curve plots  
- Filter by well, field, or production period  
- Real-time updates as parameters change  
- Modular data loading (API, S3, Snowflake-ready)  
- Caching and async processing for better performance  

## Requirements

- Python 3.8+  
- pip  

## Setup

Clone the repository:

```bash
git clone https://github.com/brainopensource/WellLit.git
cd WellLit
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or use the batch script:

```bash
install.bat
```

## Running the App

To run the app manually:

```bash
python -m streamlit run src/app.py
```

Or use the batch script:

```bash
run.bat
```

## Project Structure

```
/src
├── app.py         – Main Streamlit app  
├── data/          – Data loaders (API, S3, etc.)  
├── components/    – UI components  
├── utils/         – Decline curve calculations  
/assets            – Static files  
/cache             – Optional cached data  
```

## License

MIT License © Brain OpenSource
