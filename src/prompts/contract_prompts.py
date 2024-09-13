CONTRACT_DESIGN_PROMPT = """
Given the following requirements, design a Clarity smart contract:

Requirements:
{requirements}

Please provide a detailed Clarity smart contract that includes:
1. Appropriate data vars and maps
2. Relevant functions with proper access controls
3. Error handling
4. Any necessary helper functions
5. Comments explaining the purpose of each section

Ensure the contract follows best practices for security and efficiency in Clarity.
"""

CONTRACT_OPTIMIZATION_PROMPT = """
Review and optimize the following Clarity smart contract:

{contract}

Please provide an optimized version of the contract, focusing on:
1. Gas efficiency
2. Security improvements
3. Code readability
4. Any potential logical errors or edge cases

Explain your optimizations and why they improve the contract.
"""

TEST_GENERATION_PROMPT = """
Given the following Clarity smart contract, generate a comprehensive test suite:

{contract}

Your test suite should include:
1. Unit tests for each public function
2. Tests for edge cases and potential error conditions
3. Tests for different user roles (if applicable)
4. Tests for any complex logic or calculations

Provide the test cases in a format compatible with the Clarity testing framework, including setup, execution, and assertions for each test.
"""