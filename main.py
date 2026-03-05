import fastapi
import numpy
import pandas
import matplotlib
import genai

from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEN_AI_KEY")
