import json
import argparse
import sys
from typing import Any, List, Union, Dict

def get_hashable(item: Any) -> Any:
    """Convert non-hashable items (dicts, lists) into hashable ones for comparison."""
    if isinstance(item, dict):
        return tuple(sorted((k, get_hashable(v)) for k, v in item.items()))
    if isinstance(item, list):
        return tuple(get_hashable(i) for i in item)
    return item

def deduplicate(data: Any) -> Any:
    """Recursively deduplicate lists within the JSON structure."""
    if isinstance(data, list):
        seen = set()
        new_list = []
        for item in data:
            # Process nested structures first
            processed_item = deduplicate(item)
            # Create a hashable version for the 'seen' set
            hashable_item = get_hashable(processed_item)
            if hashable_item not in seen:
                seen.add(hashable_item)
                new_list.append(processed_item)
        return new_list
    
    if isinstance(data, dict):
        return {k: deduplicate(v) for k, v in data.items()}
    
    return data

def main():
    parser = argparse.ArgumentParser(description="Deduplicate large JSON files.")
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("output", help="Path to output JSON file")
    
    args = parser.parse_args()

    try:
        print(f"Reading {args.input}...")
        with open(args.input, 'r') as f:
            # Using standard json.load for 100k tokens (approx 400KB-1MB) is fine.
            # For multi-GB files, we'd use ijson.
            data = json.load(f)
        
        print("Deduplicating...")
        deduped_data = deduplicate(data)
        
        print(f"Writing to {args.output}...")
        with open(args.output, 'w') as f:
            json.dump(deduped_data, f, indent=2)
        
        print("Done!")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
