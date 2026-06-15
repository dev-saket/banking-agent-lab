from dotenv import load_dotenv
from pydantic_ai.models.groq import GroqModel


load_dotenv()

GROQ_MODEL = GroqModel("llama-3.3-70b-versatile")