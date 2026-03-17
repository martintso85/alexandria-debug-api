# Alexandria Debug API Starter

## Setup on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

## Test analyze API

Use `tests/sample_request.json` with Swagger UI or Postman.
