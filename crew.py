from crewai import Agent, Task, Crew
import os

# ⚠️ Assure-toi d’avoir défini OPENAI_API_KEY dans Render (Environment Variables)

# Création d’un agent simple
assistant_agent = Agent(
    role="AI Assistant",
    goal="Répondre aux questions de l'utilisateur de manière claire et concise.",
    backstory="Un assistant virtuel conçu pour aider les développeurs et créateurs.",
    verbose=True
)

# Définir une tâche type
def create_task(user_input: str):
    return Task(
        description=f"Répondre à la question suivante : {user_input}",
        agent=assistant_agent
    )

# Crew = regroupement d’agents + logique d’exécution
def run_crew(user_input: str):
    task = create_task(user_input)
    crew = Crew(agents=[assistant_agent], tasks=[task])
    result = crew.kickoff()
    return result
