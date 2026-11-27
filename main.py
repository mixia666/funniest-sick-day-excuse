"""The Funniest Sick-Day Excuse.

Writes one line (under 200 characters) to /output/entry.txt: a sick-day
excuse with a half-believable medical core, a visual gag in the middle,
and the punchline saved for the very end.
"""

import os

EXCUSE = (
    "Can't come in today \u2014 one sneeze threw my back out and now I'm "
    "stuck bent like a question mark; my doctor prescribed rest, fluids, "
    "and absolutely no contact with my inbox."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
