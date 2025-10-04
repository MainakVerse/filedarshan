# AI File Summarizer

`filedarshan` is a simple command-line tool to **summarize files and folders using AI**. It scans a file or directory, extracts metadata, and provides a human-readable summary using AI models like **Gemini**.

---

## 🔹 Features

- Summarizes **files** (CSV, TXT, JSON, Python scripts, etc.)  
- Analyzes **folders** and shows file counts by type  
- Optional **AI-powered summary** for better understanding  
- Simple CLI interface  

---

## 🔹 Installation

```bash
pip install filedarshan

```

## 🔹 Usage

# Summarize a single file
ai-file-summarizer ./data.csv

# Summarize a folder
ai-file-summarizer ./my_project_folder



## 🔹 Example Output


📊 Metadata:
{
  "name": "data.csv",
  "size_kb": 512,
  "type": "text/csv",
  "columns": ["id", "name", "age", "salary"],
  "rows_estimate": 10000
}

🤖 AI Summary:
The file `data.csv` contains 10,000 records with 4 columns (`id`, `name`, `age`, `salary`).
It appears to be a dataset for employee or user information.
