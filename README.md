# 🐾 JSON Deduplicator

A lightweight, powerful tool to recursively deduplicate large JSON structures. It removes identical items from arrays at any nesting level.

## 🚀 Features
- **Deep Comparison**: Detects identical objects and arrays regardless of nesting.
- **Web Interface**: A clean, modern UI for browser-based deduplication.
- **CLI Utility**: A Python script for batch processing large files.
- **Performance**: Optimized for large JSON files (100k+ tokens).

## 🛠 Usage

### Web Interface
Simply open `dedupe.html` in any modern browser. 
- Paste your JSON or upload a `.json` file.
- Click **Deduplicate Now**.
- Download the cleaned result.

### CLI (Python)
```bash
python3 dedupe.py input.json output.json
```

## 📂 Project Structure
- `dedupe.html`: The browser-based tool (HTML/JS/CSS).
- `dedupe.py`: The Python CLI utility.

## 📄 License
MIT
