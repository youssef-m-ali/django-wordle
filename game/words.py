from pathlib import Path
import random


_WORDS: list[str] | None = None


def load_words() -> list[str]:
    global _WORDS
    if _WORDS is None:
        path = Path(__file__).with_name("words.txt")
        with path.open() as f:
            _WORDS = [
                stripped.lower()
                for line in f
                if (stripped := line.strip())
                and len(stripped) == 5
                and stripped.isalpha()
            ]
    return _WORDS


def random_solution() -> str:
    words = load_words()
    return random.choice(words)


def is_valid_word(word: str) -> bool:
    """
    Validate a player's guess:
    - must be exactly 5 characters
    - must be alphabetic
    We do NOT require it to be in the solution word list.
    """
    word = word.lower().strip()
    return len(word) == 5 and word.isalpha()

