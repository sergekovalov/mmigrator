import re
import json


def try_load_from_json(varname: str, data: str) -> str | None:
    data = json.loads(data)
    return data.get(varname)


def try_load_from_dotenv(varname: str, data: str) -> str | None:
    m = re.search(fr'{varname}\s?=\s?(.+)', data)
    return m[1] if m else None


def load_var(filename: str, varname: str) -> str:
    var_value = None

    with open(filename, 'r') as f:
        data = f.read()

    if re.match(r'^.*\.json$', filename):
        var_value = try_load_from_json(varname, data)
    else:
        var_value = try_load_from_dotenv(varname, data)

    if not var_value:
        raise Exception(f'Cannot parse {varname} variable from file {filename}')

    return var_value
