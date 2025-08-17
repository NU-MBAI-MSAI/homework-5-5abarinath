def date_format(unformatted_date: str) -> str:
    parts = unformatted_date.split('/')
    if(len(parts) != 3):
        return False
    return f"{parts[2]}-{parts[0]}-{parts[1]}"