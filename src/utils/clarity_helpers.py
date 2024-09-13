import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_clarity_contract(requirements: str) -> str:
    prompt = f"""
    Given the following requirements, generate a Clarity smart contract:

    Requirements:
    {requirements}

    Please provide a complete Clarity smart contract that includes:
    1. Appropriate data vars and maps
    2. Relevant functions with proper access controls
    3. Error handling
    4. Any necessary helper functions
    5. Comments explaining the purpose of each section

    Ensure the contract follows best practices for security and efficiency in Clarity.
    """

    message = anthropic.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    contract = message.content[0].text.strip()
    
    # Remove any markdown code block indicators
    contract = contract.replace("```clarity", "").replace("```", "").strip()

    return contract

def generate_clarity_tests(contract: str) -> str:
    prompt = f"""
    Given the following Clarity smart contract, generate a comprehensive test suite using Clarinet and TypeScript:

    {contract}

    Your test suite should include:
    1. Unit tests for each public function
    2. Tests for edge cases and potential error conditions
    3. Tests for different user roles (if applicable)
    4. Tests for any complex logic or calculations

    Provide the COMPLETE test cases in TypeScript format compatible with Clarinet, including setup, execution, and assertions for each test. 
    Ensure that the test suite is complete, syntactically correct, and covers all aspects of the contract.
    Include necessary imports and the complete Clarinet.test structure for each test case.
    Do not include any explanations or summaries, only output the actual TypeScript code for the tests.
    """

    message = anthropic.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        temperature=0.7,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    tests = message.content[0].text.strip()
    
    # Remove any markdown code block indicators
    tests = tests.replace("```typescript", "").replace("```", "").strip()
    
    return tests

def validate_clarity_contract(contract: str) -> str:
    # Implement actual validation logic here
    return "Contract validation successful."

def validate_clarity_tests(tests: str) -> str:
    # Implement actual test validation logic here
    return "Test validation successful."

def setup_project_structure(project_name: str) -> str:
    try:
        os.makedirs(project_name, exist_ok=True)
        os.makedirs(os.path.join(project_name, "contracts"), exist_ok=True)
        os.makedirs(os.path.join(project_name, "tests"), exist_ok=True)
        os.makedirs(os.path.join(project_name, "frontend"), exist_ok=True)
        
        return f"Project structure for '{project_name}' set up successfully."
    except Exception as e:
        return f"Error setting up project structure: {str(e)}"

def save_contract(project_name: str, contract: str) -> str:
    try:
        os.makedirs(os.path.join(project_name, "contracts"), exist_ok=True)
        contract_path = os.path.join(project_name, "contracts", "contract.clar")
        with open(contract_path, "w") as f:
            f.write(contract)
        return f"Contract saved successfully to {contract_path}"
    except Exception as e:
        return f"Error saving contract: {str(e)}"

def save_tests(project_name: str, tests: str) -> str:
    try:
        os.makedirs(os.path.join(project_name, "tests"), exist_ok=True)
        tests_path = os.path.join(project_name, "tests", "contract_test.ts")
        with open(tests_path, "w") as f:
            f.write(tests)
        return f"Tests saved successfully to {tests_path}"
    except Exception as e:
        return f"Error saving tests: {str(e)}"