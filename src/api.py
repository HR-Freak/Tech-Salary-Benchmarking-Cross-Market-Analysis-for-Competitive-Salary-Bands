import os
import json
from pathlib import Path
import requests

BASE_URL = "https://api.openwebninja.com/job-salary-data/job-salary"
HEADERS = {
    "x-api-key": os.getenv("JSEARCH_API_KEY", "").strip()
}  

RAW_DIR = Path("data/raw_api")
RAW_DIR.mkdir(parents=True, exist_ok=True)


def get_salary_estimate(job_title, location, years_experience=None):
    params = {
        "job_title": job_title,
        "location": location
    }
    if years_experience is not None:
        params["years_experience"] = years_experience

    r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def save_raw(payload, filename):
    filepath = RAW_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return filepath


def fetch_role_location(role, location, years_experience=None, force_refresh=False):
    safe_role = role.lower().replace(" ", "_").replace("/", "_")
    safe_location = location.lower().replace(" ", "_").replace("/", "_")
    years_tag = "na" if years_experience is None else str(years_experience)
    filename = f"{safe_role}__{safe_location}__y{years_tag}.json"

    filepath = RAW_DIR / filename

    if filepath.exists() and not force_refresh:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    payload = get_salary_estimate(role, location, years_experience)
    save_raw(payload, filename)
    return payload


def extract_rows(payload):

    if isinstance(payload, dict):
        data = payload.get("data", [])
        if isinstance(data, dict):
            data = [data]

    elif isinstance(payload, list):
        data = payload
    else:
        return []

    rows = []
    for item in data:
        rows.append({
            "job_title": item.get("job_title"),
            "location": item.get("location"),
            "min_salary": item.get("min_salary"),
            "max_salary": item.get("max_salary"),
            "avg_salary": item.get("avg_salary"),
            "currency": item.get("currency"),
            "salary_period": item.get("salary_period"),
            "confidence": item.get("confidence"),
            "publisher_name": item.get("publisher_name"),
        })
    return rows