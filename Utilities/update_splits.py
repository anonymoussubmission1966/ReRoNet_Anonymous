import json
from pathlib import Path

# File paths
INPUT_JSON = "ANONYMOUS.json"  # Replace with your input JSON filename
OUTPUT_JSON = r"ANONYMOUS.json"

OLD_PREFIX = "ANONYMOUS"
NEW_PREFIX = "ANONYMOUS"


def update_paths(data):
    """Recursively traverses JSON data structure to update matching path strings."""
    if isinstance(data, dict):
        return {k: update_paths(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [update_paths(item) for item in data]
    elif isinstance(data, str) and OLD_PREFIX in data:
        # Convert Windows backslashes to Linux forward slashes for the updated path
        updated_path = data.replace(OLD_PREFIX, NEW_PREFIX).replace("\\", "/")
        return updated_path
    return data


def main():
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    updated_dataset = update_paths(dataset)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(updated_dataset, f, indent=2)

    print(f"[SUCCESS] Updated JSON written to: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()