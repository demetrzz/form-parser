from fastapi import FastAPI, Depends
from tinydb import TinyDB
from typing import Dict
import re
from starlette.requests import Request

app = FastAPI()
db = TinyDB('db.json')


def parse_query_params(request: Request):
    data = dict(request.query_params)
    validated_data = {}
    for key, value in data.items():
        if re.match(r"\d{2}\.\d{2}\.\d{4}", value) or re.match(r"\d{4}-\d{2}-\d{2}", value):
            validated_data[key] = 'date'
        elif re.match(r"\+7 \d{3} \d{3} \d{2} \d{2}", value):
            validated_data[key] = 'phone'
        elif re.match(r"[^@]+@[^@]+\.[^@]+", value):
            validated_data[key] = 'email'
        else:
            validated_data[key] = 'text'
    return validated_data


@app.post("/get_form/")
def get_form(validated_data: Dict[str, str] = Depends(parse_query_params)):
    max_matches = 0
    best_template = None
    for template in db.all():
        matches = sum(key in validated_data and validated_data[key] == value
                      for key, value in template['template'].items() if key != 'name')
        if matches > max_matches:
            max_matches = matches
            best_template = template
    if best_template is not None:
        return {"template_name": best_template['template']['name']}
    return validated_data
