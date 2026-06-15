from dotenv import load_dotenv
from pydantic_ai.models.groq import GroqModel


load_dotenv()

MODEL = GroqModel("llama-3.3-70b-versatile")