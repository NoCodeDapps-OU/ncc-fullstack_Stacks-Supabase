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