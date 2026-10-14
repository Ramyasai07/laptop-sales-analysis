# Laptop Sales Analysis

A Flask-based REST API that predicts laptop prices using a Linear Regression model trained on a small sample dataset.

## Features

- Health-check endpoint to verify API availability.
- Laptop price prediction using RAM, SSD capacity, and CPU score.
- Automated tests using pytest.
- Code coverage reporting.
- GitHub Actions CI for build, lint, and test checks.
- Docker support.

## Tech Stack

- Python
- Flask
- NumPy
- scikit-learn
- pytest
- Docker
- GitHub Actions

## Setup

Clone the repository:

```bash
git clone https://github.com/Ramyasai07/laptop-sales-analysis.git
cd laptop-sales-analysis
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

```bash
python -m flask --app app.main run
```

The API runs locally at `http://127.0.0.1:5000`.

## API Endpoints

### Health Check

`GET /health`

Example response:

```json
{
  "status": "ok"
}
```

### Predict Laptop Price

`POST /predict`

Example request:

```json
{
  "ram": 16,
  "ssd": 512,
  "cpu_score": 8
}
```

Returns a predicted laptop price as JSON.

## Run Tests

```bash
pytest --cov=app
```

## Docker

Build the image:

```bash
docker build -t laptop-sales-analysis .
```

Run the container:

```bash
docker run -p 5000:5000 laptop-sales-analysis
```

## Note

The model uses a tiny sample training dataset for demonstration purposes. Its predictions are not intended to represent actual market prices.
