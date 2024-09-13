# NOCC full stack app generator

## Installation

Clone the repository:
```
git clone https://github.com/NoCodeClarity-OU/ncc-fullstack.git
cd ncc-smartcontract
```

Install dependencies using Poetry:
```
pip install requirements.txt 
```

## Usage
Create a `.env` file in the project root and add your Anthropic API keys:
```
ANTHROPIC_API_KEY=<your_anthropic_api_key>
```

## Project Structure
```
ncc-smartcontract/
├── src/
│   ├── init.py
│   ├── agents.py
│   ├── crews.py
│   ├── tasks.py
│   ├── tools.py
│   ├── prompts/
│   │   ├── init.py
│   │   ├── contract_prompts.py
│   │   ├── frontend_prompts.py
│   │   └── test_prompts.py
│   └── utils/
│       ├── init.py
│       └── clarity_helpers.py
│       └── frontend_helpers.py
├── tests/
│   ├── init.py
│   └── test_contract_generation.py
├── .env
├── main.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

To run the AI agent:
Lock poetry dependencies:
```
poetry lock
```
install dependencies:
```
poetry install
```

Activate the Poetry virtual environment:
```
poetry shell
```

Run the main script:
```
python main.py
```


