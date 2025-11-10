# recap.py

import argparse
import openai
from datetime import datetime

# === CONFIG ===
openai.api_key = "your-api-key-here"  # Use environment variable in production
DEFAULT_STYLE = "professional"
SUPPORTED_PLATFORMS = ["linkedin", "twitter", "instagram"]
OUTPUT_FORMATS = ["text", "markdown", "html"]

# === CORE FUNCTIONS ===

def load_input(source):
    """Load input from file or direct text"""
    if source.endswith(".txt"):
        with open(source, "r", encoding="utf-8") as f:
            return f.read()
    return source

def summarize_text(text):
    """Summarize using OpenAI GPT"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize this content in 3–5 sentences."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_post(summary, platform="linkedin", style=DEFAULT_STYLE):
    """Generate platform-specific post using OpenAI"""
    prompt = f"Write a {style} social media post for {platform} based on this summary:\n\n{summary}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def format_output(post, format="text"):
    """Format post for GitHub Pages or other outputs"""
    if format == "markdown":
        return f"### Social Post\n\n{post}"
    elif format == "html":
        return f"<h3>Social Post</h3>\n<p>{post}</p>"
    return post

# === CLI INTERFACE ===

def main():
    parser = argparse.ArgumentParser(description="Fusion Social Post Writer Agent")
    parser.add_argument("source", help="Text input or path to .txt file")
    parser.add_argument("--platform", choices=SUPPORTED_PLATFORMS, default="linkedin")
    parser.add_argument("--style", default=DEFAULT_STYLE)
    parser.add_argument("--format", choices=OUTPUT_FORMATS, default="text")

    args = parser.parse_args()
    raw_text = load_input(args.source)
    summary = summarize_text(raw_text)
    post = generate_post(summary, args.platform, args.style)
    formatted = format_output(post, args.format)

    print("\nGenerated Social Post:\n")
    print(formatted)

if __name__ == "__main__":
    main()
