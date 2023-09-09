from dataclasses import dataclass

@dataclass
class ParsedData:
    link: str
    text: list[str]