import os

from dotenv import load_dotenv

# .env ファイルを読み込む
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
