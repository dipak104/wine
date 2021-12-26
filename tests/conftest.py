import pytest
import yaml
import os
import json
from src.get_data import read_params

@pytest.fixture
def config(config_path="params.yaml"):
    config = read_params(config_path)
    return config

@pytest.fixture
def schema_in(schema_path="schema_in.json"):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema