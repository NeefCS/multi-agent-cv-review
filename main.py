from navaia_forge import NavaiaForgeClient
import os


client = NavaiaForgeClient(
    base_url="https://api.navaia.com", #http://localhost:8001 ، https://fareegi.navaia.sa
    api_key = os.getenv("NAVAIA_API_KEY")
)

workforce = client.workforces.create(name = "CV review workforce", runtime_mode="claude_max",)
print(f"Workforce: {workforce['id']}")

## agents:
analizer_ag = client.agents.create(
    workforce_id = workforce.id,
    name = "CV analizer agent",
    role = "analizer",
    instructions = "Agent responsible for analyzing CVs and extracting relevant information such as skills, experience, and education.",
    model_provider = "anthropic",
    model_name = "sonnet",
    # model_name ="claude-sonnet-4-6",
    # model_provider = "openai",
    # model_name = "gpt-5-codex",
)

evaluator_ag = client.agents.create(
    workforce_id = workforce.id,
    name = "CV evaluator agent",
    role = "evaluator",
    instructions = "Agent responsible for evaluating the extracted information from CVs and providing a score for each candidate based on predefined criteria.",
    model_provider = "anthropic",
    model_name = "sonnet",
    # model_name = "claude-sonnet-4-6",
    # model_provider = "openai",
    # model_name = "gpt-5-codex",
)

advisor_ag = client.agents.create(
    workforce_id = workforce.id,
    name = "CV advisor agent",
    role = "advisor",
    instructions = "Agent responsible for providing feedback and recommendations to candidates based on the evaluation results.",
    model_provide = "anthropic",
    model_name = "sonnet",
    # model_name= "claude-sonnet-4-6",
    # model_provider = "openai",
    # model_name = "gpt-5-codex",
)


client.workforces.edges.create(
    workforce_id=workforce.id,
    source_agent_id=analizer_ag.id,
    target_agent_id=evaluator_ag.id,
)
client.workforces.edges.create(
    workforce_id=workforce.id,
    source_agent_id=evaluator_ag.id,
    target_agent_id=advisor_ag.id,
)


cv_text = """
Name: Naif Alhammad
Email: naif@example.com
Education: BSc Computer Science, King Fahd University, 2020
Experience:
  - Software Engineer at STC, 2020-2023 (Python, AWS)
  - Backend Developer at Elm, 2023-present (Docker)
Skills: Python, AWS, Docker
"""

task = client.tasks.create(
    workforce_id = workforce.id,
    agent_id = analizer_ag.id,
    title = "Review CV for Computer Science Position",
    description = f"Review the following CV and provide detailed feedback:\n\n{cv_text}",
)


#result
print("reviewing...")
final = client.tasks.wait_for_completion(task.id)

# print("Full task details:")
# print(vars(final))
print("Status: ", final.status)
print("Result: ", final.result)
