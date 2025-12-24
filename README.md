🤖 AI Tools Harvester

AI Tools Harvester is an Apify Actor that discovers, extracts and scores AI tools from the web, producing a clean, structured dataset ready for analysis, research, or integration into other systems.
The actor empowers teams to stay ahead in the fast-moving AI ecosystem by automatically discovering, scoring, and organizing AI tools—making it easy to compare options, align tools with workflows and adopt the best solutions without manual research.
It is also designed for developers, founders and researchers who need an automated way to collect up-to-date information about AI tools across the ecosystem.

🚀 What this Actor does

🔍 Crawls web sources to discover AI tools

🧠 Extracts key metadata for each tool

📊 Assigns a relevance score to help rank results

🗂️ Stores results in a structured Apify Dataset

🖥️ Presents output in a clean, table-based UI

Each run produces a dataset where each item represents one AI tool.

📦 Output dataset structure
Each dataset item contains the following fields:

  Field	Type	Description
  name	string	Name of the AI tool
  website	string (URL)	Official website of the tool
  category	string	Category or use case
  score	number	Relevance score assigned by the Actor

The dataset schema is fully defined, so results are displayed in a friendly table view in the Apify Console and export cleanly to CSV, Excel, JSON and more.

🧩 Example output
{
  "name": "Example AI Tool",
  "website": "https://example-ai.com",
  "category": "Productivity",
  "score": 70
}

🛠️ How it works 
The Actor navigates target pages using browser automation
Relevant AI tool information is extracted
Tools are evaluated and assigned a relevance score
Results are stored in the default Apify Dataset
The dataset is rendered using a predefined dataset schema

📤 Exporting results

You can export the dataset in multiple formats:
JSON / JSONL
CSV
Excel
XML
HTML table
RSS

Exports are available directly from the Dataset tab or via the Apify API.

🧪 Use cases
Tracking emerging AI products
Market research and competitive analysis
Powering search, ranking or recommendation systems
Feeding AI tool data into internal dashboards
Building AI tool directories

🔐 Permissions & safety
Uses standard Apify storages (Dataset, Request Queue)
Does not require special permissions
Designed to run within Apify’s platform limits

🧠 Author
Created by radiating_nucleus
Published on Apify Store

📌 Notes
The Actor produces structured, schema-validated output
Dataset schema ensures consistent UI visualization
Suitable for both one-off runs and automation pipelines
