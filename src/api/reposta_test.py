response = [
    {
        "id": "1",
        "name": "Anakin Skywalker",
        "email": "skywalker@ssys.com.br",
        "department": "Architecture",
        "salary": "4000.00",
        "birth_date": "01-01-1983"
    },
    {
        "id": "2",
        "name": "Obi-Wan Kenobi",
        "email": "kenobi@ssys.com.br",
        "department": "Back-End",
        "salary": "3000.00",
        "birth_date": "01-01-1977"
    },
    {
        "id": "3",
        "name": "Leia Organa",
        "email": "organa@ssys.com.br",
        "department": "DevOps",
        "salary": "5000.00",
        "birth_date": "01-01-1980"
    }
]


def get_lowest_salary() -> dict:
    result = None
    for r in response:
        if result is not None and r['salary'] > result['salary']:
            continue
        result = r
    return result


def get_highest_salary() -> dict:
    result = None
    for r in response:
        if result is not None and r['salary'] < result['salary']:
            continue
        result = r
    return result


def get_older() -> dict:
    result = None
    for r in response:
        if result is not None and r['birth_date'] > result['birth_date']:
            continue
        result = r
    return result


def get_younger() -> dict:
    result = None
    for r in response:
        if result is not None and r['birth_date'] < result['birth_date']:
            continue
        result = r
    return result
