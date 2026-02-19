# Omni-Tools - Comprehensive Utility Set

A collection of versatile tools for common tasks. Each tool is documented with purpose, usage, and parameters.

---

## 📊 System Tools

### 1. `system_status`
**Purpose:** Get comprehensive system health overview
**Usage:** `system_status`
**Returns:** CPU, RAM, Disk, Network, Process stats
**Notes:** Quick health check before heavy operations

### 2. `memory_sweep`
**Purpose:** Clean up stale memory entries
**Usage:** `memory_sweep [days=30]`
**Parameters:**
- `days` - Age threshold (default: 30 days)
**Notes:** Run periodically to keep memory lean

### 3. `log_rotate`
**Purpose:** Rotate log files to prevent disk fill
**Usage:** `log_rotate [max_size=100MB] [keep=5]`
**Parameters:**
- `max_size` - Max file size before rotation (default: 100MB)
- `keep` - Number of rotated files to keep (default: 5)
**Notes:** Run as cron job weekly

---

## 🔍 Search & Discovery

### 4. `deep_search`
**Purpose:** Multi-source search across web and local files
**Usage:** `deep_search "query"`
**Returns:** Ranked results from web + local memory + project files
**Notes:** Combines web_search + memory_search + file grep

### 5. `context_search`
**Purpose:** Find context around specific topics
**Usage:** `context_search "topic" [depth=5]`
**Parameters:**
- `depth` - Number of recent memory entries to include
**Notes:** Great for "what was I thinking about X recently?"

### 6. `history_trail`
**Purpose:** Trace evolution of an idea/concept
**Usage:** `history_trail "concept"`
**Returns:** Chronological notes about the concept
**Notes:** Shows how thoughts developed over time

---

## 📝 File Operations

### 7. `quick_create`
**Purpose:** Create template-based files instantly
**Usage:** `quick_create [template] [filename]`
**Templates:**
- `md_note` - Markdown note with date header
- `todo_list` - Todo list with checkboxes
- `meeting_notes` - Meeting template
- `project_setup` - Project skeleton
**Notes:** Saves time on repetitive file creation

### 8. `file_pack`
**Purpose:** Compress multiple files into archive
**Usage:** `file_pack "files" [output.zip]`
**Parameters:**
- `files` - Comma-separated list or glob pattern
- `output` - Output filename (optional)
**Notes:** Great for sharing work snapshots

### 9. `file_extract`
**Purpose:** Extract specific content from files
**Usage:** `file_extract "path" [pattern] [output.txt]`
**Parameters:**
- `pattern` - Regex or keyword to extract
- `output` - Save to file (optional)
**Notes:** Pulls relevant snippets, ignores noise

---

## 🌐 Network Tools

### 10. `ping_check`
**Purpose:** Check connectivity to hosts
**Usage:** `ping_check "host" [count=4]`
**Parameters:**
- `host` - Domain or IP
- `count` - Pings to send (default: 4)
**Returns:** Latency, packet loss, success/fail
**Notes:** Quick connectivity verification

### 11. `port_scan`
**Purpose:** Check if ports are open
**Usage:** `port_scan "host" [ports=22,80,443]`
**Parameters:**
- `ports` - Comma-separated port list
**Notes:** Useful for service discovery

### 12. `dns_lookup`
**Purpose:** Resolve domain to IP
**Usage:** `dns_lookup "domain"`
**Returns:** A, AAAA, CNAME, MX records
**Notes:** Troubleshooting DNS issues

---

## ⚡ Automation

### 13. `batch_process`
**Purpose:** Run command on multiple files
**Usage:** `batch_process "command" "files"`
**Parameters:**
- `command` - Shell command (supports {f} placeholder)
- `files` - Glob pattern or file list
**Example:** `batch_process "echo {f}" "*.md"`
**Notes:** Great for bulk operations

### 14. `timer_task`
**Purpose:** Schedule delayed actions
**Usage:** `timer_task "message" [seconds]`
**Parameters:**
- `message` - What to do when timer expires
- `seconds` - Delay in seconds
**Notes:** One-shot reminder, saved to memory

### 15. `cron_builder`
**Purpose:** Generate cron expressions
**Usage:** `cron_builder "schedule"`
**Formats:**
- `@hourly`, `@daily`, `@weekly`, `@monthly`
- `every 5 hours`
- `at 9am every Monday`
**Notes:** Creates cron job definitions

---

## 🎨 Formatting & Display

### 16. `pretty_print`
**Purpose:** Format data for readability
**Usage:** `pretty_print "data"`
**Returns:** Colored, structured output
**Notes:** Makes logs and outputs easier to read

### 17. `table_view`
**Purpose:** Display data as table
**Usage:** `table_view "key:value" "key:value"`
**Parameters:** Multiple key:value pairs
**Notes:** Structured data visualization

### 18. `code_block`
**Purpose:** Wrap code in syntax-highlighted block
**Usage:** `code_block "language" "code"`
**Parameters:**
- `language` - Programming language
- `code` - Code to format
**Notes:** Perfect for documentation

---

## 📱 Communication

### 19. `smart_notify`
**Purpose:** Send contextual notifications
**Usage:** `smart_notify "message" [priority=normal]`
**Parameters:**
- `priority` - passive/active/timeSensitive
**Notes:** Routes to appropriate channel

### 20. `summary_gen`
**Purpose:** Generate concise summaries
**Usage:** `summary_gen "text"`
**Returns:** Key points in bullet format
**Notes:** Great for meeting recaps

---

## 🛡️ Safety & Cleanup

### 21. `trash_safe`
**Purpose:** Move files to trash (recoverable)
**Usage:** `trash_safe "files"`
**Parameters:**
- `files` - Glob pattern or file list
**Notes:** Safer than rm, files can be restored

### 22. `disk_cleanup`
**Purpose:** Clean up temporary files
**Usage:** `disk_cleanup [type=all]`
**Types:**
- `cache` - Browser/cache
- `logs` - Log files
- `temp` - Temporary files
- `all` - Everything (safe)
**Notes:** Run weekly to keep system clean

---

## 📄 PDF Tools

### 30. `pdf_merge`
**Purpose:** Combine multiple PDF files into a single PDF.
**Usage:** `pdf_merge "input1.pdf" "input2.pdf" [output.pdf]`
**Parameters:**
- `files` - Comma-separated list of input PDF file paths
- `output` - Output filename (optional, default: `merged.pdf`)
**Notes:** Merges PDFs in the order provided.

### 31. `photos_to_pdf`
**Purpose:** Convert a collection of image files (JPG, PNG, etc.) into a single PDF.
**Usage:** `photos_to_pdf "image1.jpg" "image2.png" [output.pdf]`
**Parameters:**
- `files` - Comma-separated list of input image file paths
- `output` - Output filename (optional, default: `images.pdf`)
**Notes:** Supports common image formats. Each image becomes a page in the PDF.

### 23. `resource_monitor`
**Purpose:** Track system resource usage
**Usage:** `resource_monitor [interval=5] [duration=60]`
**Parameters:**
- `interval` - Seconds between checks
- `duration` - Total monitoring time
**Returns:** Charts of CPU, RAM, Disk, Network
**Notes:** Great for profiling long-running tasks

### 24. `process_tree`
**Purpose:** Show process hierarchy
**Usage:** `process_tree [pid]`
**Parameters:**
- `pid` - Parent process ID (optional)
**Notes:** Find what's consuming resources

---

## 🧩 Utility

### 25. `json_pretty`
**Purpose:** Format JSON for readability
**Usage:** `json_pretty "json_string"`
**Returns:** Pretty-printed JSON
**Notes:** Debugging API responses

### 26. `url_encode`
**Purpose:** URL-encode strings
**Usage:** `url_encode "text"`
**Returns:** URL-safe string
**Notes:** For API calls, form submissions

### 27. `base64_decode`
**Purpose:** Decode Base64 strings
**Usage:** `base64_decode "encoded"`
**Returns:** Decoded text
**Notes:** Decode data from various sources

---

## 📚 Documentation

### 28. `doc_gen`
**Purpose:** Generate documentation from code/comments
**Usage:** `doc_gen "path" [format=md]`
**Parameters:**
- `format` - markdown or html
**Notes:** Auto-documents project structure

### 29. `readme_builder`
**Purpose:** Create project README
**Usage:** `readme_builder "project"`
**Parameters:**
- `project` - Project name
**Notes:** Generates starter README with sections

---

## Usage Patterns

### Quick Start (Every Session)
```bash
system_status              # Check system health
deep_search "what do I need to do today?"  # Find tasks
```

### Daily Routine
```bash
memory_sweep               # Clean old memories
log_rotate                 # Rotate logs
disk_cleanup               # Clean temp files
```

### Before Big Tasks
```bash
resource_monitor           # Check resources
port_scan "target"         # Check connectivity
```

### After Work
```bash
file_pack "project"        # Save snapshot
summary_gen "today"        # Summarize day
```

---

## Implementation Notes

- All tools should save history to memory/YYYY-MM-DD.md
- Critical operations should notify user
- Safe operations should be idempotent
- Document parameters and return values
- Include examples in comments

---

*Last updated: 2026-02-19*
*Author: Clawe*
