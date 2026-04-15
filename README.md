# 🤖 AI Resume Screening System

An AI-powered Resume Screening System built with **LangChain** and **LangSmith** that evaluates candidates against a job description using a modular 4-step pipeline.

## 🏗️ Architecture

```
Resume + Job Description
        │
        ▼
┌───────────────────┐
│ Step 1: EXTRACT   │  → Skills, Experience, Tools (JSON)
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Step 2: MATCH     │  → Matched / Missing Skills (JSON)
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Step 3: SCORE     │  → Fit Score 0–100 (JSON)
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ Step 4: EXPLAIN   │  → Reasoning + Recommendation (JSON)
└───────────────────┘
```

## 📁 Project Structure

```
Resume_Traker/
├── prompts/                    # Prompt templates for each step
│   ├── extraction_prompt.py    # Skill extraction prompt
│   ├── matching_prompt.py      # Resume-JD matching prompt
│   ├── scoring_prompt.py       # Scoring prompt (0-100)
│   └── explanation_prompt.py   # Explanation generation prompt
├── chains/                     # LangChain LCEL chains
│   ├── extraction_chain.py     # Extract chain
│   ├── matching_chain.py       # Match chain
│   ├── scoring_chain.py        # Score chain
│   ├── explanation_chain.py    # Explain chain
│   └── pipeline.py             # Full pipeline orchestration
├── data/                       # Sample data
│   ├── resumes.py              # 3 resumes (strong/avg/weak)
│   └── job_description.py      # Data Scientist JD
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
├── .env.example                # Environment variable template
└── README.md                   # This file
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Resume_Traker.git
cd Resume_Traker
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
```bash
cp .env.example .env
```
Edit `.env` and add your keys:
- **Google Gemini API Key**: Get from [aistudio.google.com](https://aistudio.google.com/apikey)
- **LangSmith API Key**: Get from [smith.langchain.com](https://smith.langchain.com)

### 5. Run the System
```bash
python main.py
```

## 🔧 Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core language |
| LangChain | LLM pipeline framework |
| LangChain LCEL | Chain composition (PromptTemplate \| LLM \| Parser) |
| LangSmith | Tracing, debugging, monitoring |
| Google Gemini 2.0 Flash | Language model |
| python-dotenv | Environment variable management |

## 📊 Sample Output

The system screens 3 candidates against a Data Scientist job description:

| Candidate | Score | Category | Recommendation |
|---|---|---|---|
| Arjun Mehta (Strong) | ~85-92 | Strong | Strongly Recommend |
| Priya Sharma (Average) | ~45-60 | Average | Recommend with Reservations |
| Rahul Gupta (Weak) | ~10-25 | Weak | Do Not Recommend |

## 🔍 LangSmith Tracing

LangSmith captures every step of the pipeline:
- All 4 pipeline steps are visible per candidate run
- Each run is tagged (`strong_candidate`, `average_candidate`, `weak_candidate`)
- Input/output of each chain is logged for debugging

Access traces at: [smith.langchain.com](https://smith.langchain.com)

## 📌 Key Design Decisions

1. **Anti-hallucination**: Prompts explicitly instruct the LLM to extract ONLY stated skills
2. **Structured JSON output**: Every chain uses `JsonOutputParser` for reliable parsing
3. **Weighted scoring**: 5 dimensions with configurable weights for fair evaluation
4. **Evidence-backed explanations**: Every strength/weakness must cite specific resume data
5. **Few-shot prompting**: Extraction prompt includes an example for consistent output

## 🧪 Prompt Engineering

- Clear task instructions with strict rules
- Output schema defined in each prompt
- Anti-hallucination guardrails
- Few-shot example in extraction prompt
- Constrained scoring guidelines (80-100 = Strong, 50-79 = Average, 0-49 = Weak)

## 📝 License

This project is created for educational purposes as part of a GenAI internship assignment.

## 👤 Author

**Jakkoju Vikasraj**

---

*Built with ❤️ using LangChain + LangSmith*
