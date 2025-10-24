# fusion_writer/agent.py

from fusion_writer.prompts import announcement
from fusion_writer.personas import community_builder, hype_curator, calm_explainer
from fusion_writer.formatters import instagram, twitter, linkedin

def generate_post(data):
    post_type = data.get("type", "announcement")
    persona = data.get("persona", "community_builder")
    platform = data.get("platform", "instagram")

    # Select prompt template
    if post_type == "announcement":
        prompt = announcement.generate_announcement_prompt(data)
    else:
        raise ValueError("Unsupported post type")

    # Apply persona tone
    if persona == "community_builder":
        prompt = community_builder.apply(prompt)
    elif persona == "hype_curator":
        prompt = hype_curator.apply(prompt)
    elif persona == "calm_explainer":
        prompt = calm_explainer.apply(prompt)

    # Format for platform
    if platform == "instagram":
        return instagram.format(prompt)
    elif platform == "twitter":
        return twitter.format(prompt)
    elif platform == "linkedin":
        return linkedin.format(prompt)
    else:
        return prompt
