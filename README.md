# 📚 Learning Path Generator

## Overview

Learning a new skill can be overwhelming because learners often don't know where to start or what topics to study next. They frequently jump between tutorials, courses, and resources without a structured plan.

The Learning Path Generator solves this problem by using Generative AI to create a structured learning roadmap from a single skill or domain input. The generated roadmap organizes learning into stages, identifies important topics, and provides a concise summary of the learning journey.

---

## Problem Statement

Learners often know **what** they want to learn but struggle with **how** to learn it effectively.

Without a clear roadmap:

* Learning becomes unstructured
* Important fundamentals may be skipped
* Progress is difficult to track
* Time is spent searching for what to learn next

This project uses Google's Gemini model to automatically generate logical and progressive learning paths for any skill.

---

## Features

✅ Generate learning roadmaps for any skill or domain

✅ Create stage-wise learning progression

✅ Identify key topics in the correct learning order

✅ Generate concise learning goal summaries

✅ Download generated roadmap as JSON

✅ Simple and interactive Streamlit interface

✅ Structured output using Pydantic models

---

## Tech Stack

| Technology       | Purpose                                 |
| ---------------- | --------------------------------------- |
| Python           | Core programming language               |
| Streamlit        | User Interface                          |
| LangChain        | Prompt management and LLM orchestration |
| Gemini 2.5 Flash | Generative AI model                     |
| Pydantic         | Structured output validation            |
| Python Dotenv    | Environment variable management         |

---

## Project Structure

```text
learning_path_generator/
│
├── app.py
├── prompts.py
├── roadmap_generator.py
│
├── requirements.txt
├── .env
└── README.md
```

### File Description

#### app.py

Handles the Streamlit user interface.

Responsibilities:

* Accept user input
* Trigger roadmap generation
* Display learning stages
* Display key topics
* Show learning summary
* Allow JSON download

#### prompts.py

Contains the prompt template used by the Gemini model.

Responsibilities:

* Define roadmap generation instructions
* Guide the model toward consistent outputs

#### roadmap_generator.py

Contains the LangChain and Gemini integration.

Responsibilities:

* Connect to Gemini
* Generate structured responses
* Validate output using Pydantic
* Return roadmap data to the UI

---

## System Workflow

```text
User Input
     │
     ▼
Prompt Template
     │
     ▼
LangChain Chain
     │
     ▼
Gemini 2.5 Flash
     │
     ▼
Structured Output (Pydantic)
     │
     ▼
Streamlit Interface
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/siddagovardhanreddy33/Learning_Path_Generator.git
cd learning-path-generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Running the Application

```bash
streamlit run learning_path_generator/app.py
```

The application will launch in your browser.

---

## Example

### Input

```text
Data Science
```

### Generated Learning Stages

* Beginner
* Intermediate
* Advanced

### Key Topics

* Python Programming
* Statistics
* Data Visualization
* Machine Learning
* Model Evaluation

### Learning Goal Summary

Learn programming fundamentals, statistical concepts, and machine learning techniques before progressing toward advanced model development and evaluation.

---

## Output Schema

```json
{
  "learning_stages": [
    "Beginner",
    "Intermediate",
    "Advanced"
  ],
  "key_topics": [
    "Python Programming",
    "Statistics",
    "Data Visualization",
    "Machine Learning"
  ],
  "learning_goal_summary": "Structured overview of the learning journey."
}
```

---

## Deployment

The application can be deployed on:

* Streamlit Community Cloud
* Render
* Railway

For deployment, configure:

```toml
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

in the platform's environment variables or secrets section.

---

## Future Improvements

* Learning duration estimation
* Visual roadmap timeline
* Course recommendations
* Personalized learning paths
* PDF export support
* Resource recommendations for each topic

---

## Author

Govardhan Reddy Sidda

Built using LangChain, Streamlit, and Google Gemini.
