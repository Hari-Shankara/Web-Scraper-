# Task 3 – Web Scraper for News Headlines

## Project Overview

This project is developed as part of the Python Developer Internship – Task 3.

The objective of this project is to scrape the top news headlines from a public news website using Python.

The program collects headlines from BBC News, displays them in the terminal, and saves them into a text file named `headlines.txt`.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- HTML
- VS Code

## Features

- Fetches website HTML using HTTP GET requests.
- Extracts headlines using BeautifulSoup.
- Removes duplicate headlines.
- Displays the collected headlines in the terminal.
- Saves headlines into a `.txt` file.
- Handles connection errors and HTTP errors.

## Project Structure

```text
Task-3-News-Scraper/
│
├── news_scraper.py
├── headlines.txt
├── requirements.txt
└── README.md
```

## Installation

### Step 1: Install Python Packages

```bash
pip install requests beautifulsoup4
```

### Step 2: Run the Program

```bash
python news_scraper.py
```

## Output

The program displays the collected news headlines in the terminal.

It also creates a file named `headlines.txt` containing the extracted headlines.

## Concepts Learned

- HTTP GET Requests
- Web Scraping
- HTML Parsing
- BeautifulSoup
- Python Requests Library
- Exception Handling
- File Handling

## Internship Task Details

**Task:** Task 3 – Web Scraper for News Headlines

**Objective:** Scrape top headlines from a news website.

**Tools:** Python, Requests, BeautifulSoup

**Deliverables:**
- Python script
- Text file containing headlines
- README documentation

## Conclusion

This project demonstrates how Python can automate data collection from a public website using Requests and BeautifulSoup.

It helped me understand HTTP requests, HTML parsing, web scraping, and file handling.

---

**Python Developer Internship – Task 3**