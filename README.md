# Winter 2025 Assignment 2
Logging is base 

logger2 is incomplete, 
featuring 
- make log file directory

How to use logger2 as import

from logger2 import write_log

write_log("Backup Or Restore Log")

## final version loggin tool is logtool.py
from logtool import writelog
## Input Handling (athapa30)

- Used `argparse` to parse command-line arguments:  
  `--backup`, `--restore`, `--source`, and `--destination`.

- Validates that `--source` and `--destination` paths exist (or are valid) before proceeding.

- If invalid or missing arguments, prints helpful error messages and usage.

- Calls `write_log()` from `logtool.py` to log backup and restore operations with timestamps.

- Follows instructions to keep code readable, modular, and documented.
