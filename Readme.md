# Island Water Flow Analysis

This project analyzes the number of grid cells in various topographical scenarios where water can flow down to both the island's northwest and southeast edges. The project is built using Django and Python, with the data sourced from a Google Sheet.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- Docker (if running via Docker)
- pip (Python package installer)

## Installation

### 1. Clone the Repository

```bash
git clone <git_repo_url>
cd island_flow_analysis
```

### 2. Set Up Google Sheets API
    Create a Google Cloud Project and enable the Google Sheets API.
    Create a service account and download the credentials.json file.
    Share your Google Sheet with the service account's email.
    Place the credentials.json file in the root of the project.

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run the Django Development Server

    python manage.py migrate
    python manage.py runserver

    Visit http://127.0.0.1:8000/ in your web browser.

## Running with Docker

### 1. Build Docker Image

    docker build -t island_flow_analysis .

### 2. Run Docker Container

    docker run -p 8000:8000 island_flow_analysis