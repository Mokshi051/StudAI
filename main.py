import sys
import os

# Ensure project root is on the path so all imports resolve
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from backend.api.app import app

if __name__ == "__main__":
    app.run(debug=True)
