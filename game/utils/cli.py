def parse_multiple_value_argument_from_str(argument_str: str) -> list[int]:
    if not argument_str:
        return []

    return [int(x) for x in argument_str.split(",") if x.strip().isdigit()]
