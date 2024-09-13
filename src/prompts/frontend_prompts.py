FRONTEND_DESIGN_PROMPT = """
Given the following requirements, design a frontend structure using HTML and Tailwind CSS:

Requirements:
{requirements}

Please provide a complete HTML file that includes:
1. Proper HTML5 structure
2. Tailwind CSS classes for styling
3. Responsive design considerations
4. Semantic HTML elements
5. Comments explaining the purpose of each section

Ensure the HTML is valid and follows best practices for modern web development.
Include a script tag for loading Tailwind CSS from a CDN.
"""

JAVASCRIPT_IMPLEMENTATION_PROMPT = """
Given the following HTML structure, generate JavaScript code to add interactivity and dynamic behavior:

{html_structure}

Please provide JavaScript code that includes:
1. Event listeners for user interactions
2. DOM manipulation to update the UI dynamically
3. Any necessary AJAX calls (you can use fetch API)
4. Error handling and input validation
5. Comments explaining the purpose of each function or section of code

Ensure the JavaScript is modern (ES6+) and follows best practices for web development.
"""

STACKSJS_INTEGRATION_PROMPT = """
Given the following frontend code, integrate Stacks.js components and functionality:

{frontend_code}

Please update the frontend code to include:
1. Necessary Stacks.js imports (use unpkg.com CDN for @stacks/connect-react, @stacks/network, and @stacks/transactions)
2. Stacks authentication flow using @stacks/connect-react
3. Functions to interact with Stacks blockchain (e.g., read from and write to smart contracts)
4. UI elements to display Stacks wallet information and transaction status
5. Error handling for Stacks-related operations
6. Comments explaining the Stacks.js integration

Ensure the integration follows best practices for Stacks.js usage and maintains the existing functionality of the frontend.
Include the following key components:
- Connect Wallet button
- Display of user's STX address when connected
- Function to call a smart contract method (e.g., 'say-gm')
- Function to read from a smart contract (e.g., 'get-gm')
- Display of contract interaction results

Use the StacksMocknet for the network configuration.
"""

CONTRACT_INTEGRATION_PROMPT = """
Given the following frontend code (with Stacks.js integrated) and Clarity smart contract, fully integrate the contract functionality into the frontend:

Frontend Code:
{frontend_code}

Clarity Smart Contract:
{contract}

Please update the frontend code to include:
1. Functions to call all the smart contract methods
2. UI elements to interact with each smart contract function (e.g., forms, buttons)
3. Display of smart contract data and transaction results
4. Error handling for contract interactions
5. Comments explaining the integration of each smart contract function

Ensure the integration follows best practices for interacting with Clarity smart contracts from a web frontend.
Update the existing Stacks.js integration to work with the specific functions of the provided smart contract.
"""