# fusion_social_agent/app.py

import logging
from agent import FusionAgent
from modules import content, scheduler, platforms

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fusion_social_agent")

def bootstrap_social_agent():
    agent = FusionAgent()

    # Register social modules
    agent.register_module("content", content)
    agent.register_module("scheduler", scheduler)
    agent.register_module("platforms", platforms)

    return agent

def simulate_social_workflow(agent: FusionAgent):
    user_id = "creator_007"
    role = "editor"
    context = {
        "brand": "ClarityFinance",
        "tone": "professional",
        "platforms": ["LinkedIn", "Instagram"],
        "campaign": "Q4 Financial Wellness",
    }

    # Assign role and context
    agent.assign_role(user_id, role)
    agent.set_session_context(user_id, context)

    # Generate and schedule post
    try:
        post = agent.execute(user_id, "content", "generate_post", topic="budgeting tips")
        print("Generated Post:", post)

        schedule = agent.execute(user_id, "scheduler", "schedule_post", post=post, time="2025-11-12T09:00:00")
        print("Scheduled:", schedule)

        publish_status = agent.execute(user_id, "platforms", "publish_post", post=post)
        print("Publish Status:", publish_status)

    except Exception as e:
        logger.error(f"Workflow error: {e}")

if __name__ == "__main__":
    agent = bootstrap_social_agent()
    simulate_social_workflow(agent)
