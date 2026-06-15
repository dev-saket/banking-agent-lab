from pydantic_ai import Agent

from shared.model import MODEL


agent = Agent(MODEL,
              system_prompt="""
              You are a banking assistant
              """)

result = agent.run_sync("What is BSB?")

print(result.output)