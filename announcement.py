# fusion_writer/prompts/announcement.py

def generate_announcement_prompt(data):
    """
    Generates a prompt for event announcements.
    Expected keys in data: event_name, date, location, tone, platform
    """
    tone = data.get("tone", "excited")
    platform = data.get("platform", "Instagram")
    event = data.get("event_name", "your event")
    date = data.get("date", "soon")
    location = data.get("location", "a local venue")

    return f"""
Write a {tone} social media post for {platform} announcing an upcoming event.

Event: {event}
Date: {date}
Location: {location}

Include emojis, a call to action, and relevant hashtags. Keep it concise and engaging.
"""