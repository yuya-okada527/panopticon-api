import os
import sys
from pathlib import Path

app_path = os.path.join(Path(__file__).resolve().parents[1], "app")

sys.path.append(app_path)
