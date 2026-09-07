import shutil
from pathlib import Path
import os

def cache_clearer():
    try:
        main_EnDek = Path(__file__).resolve().parent.parent
        for dirs,file, root in os.walk(main_EnDek):
            if dirs.endswith("__pycache__"):
                shutil.rmtree(dirs)
    except PermissionError:
        print("does not have required permission to clear cache files...")
        return False
    except Exception as e:
        print(f"An error occurred while clearing cache: {e}")
        return False
    return True