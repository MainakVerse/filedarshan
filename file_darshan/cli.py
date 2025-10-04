import sys
import json
from .summarizer import describe_file
from .ai_helper import ai_summary

def main():
    if len(sys.argv) < 2:
        print("Usage: ai-file-summarizer <path>")
        sys.exit(1)

    path = sys.argv[1]
    info = describe_file(path)
    print("📊 Metadata:")
    print(json.dumps(info, indent=2))

    # AI summary (only if API key set)
    try:
        summary = ai_summary(info)
        print("\n🤖 AI Summary:")
        print(summary)
    except Exception as e:
        print(f"\n(AI summary skipped: {e})")
