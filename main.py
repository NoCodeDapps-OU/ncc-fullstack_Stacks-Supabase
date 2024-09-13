import os
from dotenv import load_dotenv
from src.crews import SmartContractCrews, FrontendCrews
from src.tools import ContractIntegrationTools
from src.utils.clarity_helpers import save_contract, save_tests
from src.utils.frontend_helpers import save_frontend

load_dotenv()

def get_user_confirmation(message: str) -> bool:
    while True:
        user_input = input(f"{message} (yes/no): ").lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    smart_contract_crews = SmartContractCrews()
    frontend_crews = FrontendCrews()

    # Get user input
    project_name = input("Enter the name for your Clarity smart contract project: ")
    contract_requirements = input("Describe the requirements for your smart contract: ")
    frontend_requirements = input("Describe the requirements for your frontend: ")

    try:
        # Step 1: Set up the project structure
        setup_result = smart_contract_crews.project_setup_crew(project_name).kickoff()
        print("Project Setup Result:", setup_result)
        if not get_user_confirmation("Do you want to proceed with contract generation?"):
            return

        # Step 2: Generate the contract
        contract_result = smart_contract_crews.contract_design_crew(contract_requirements).kickoff()
        print("Contract Design Result:", contract_result)
        if not get_user_confirmation("Do you want to proceed with saving the contract?"):
            return

        # Extract the contract from the contract_result
        contract = str(contract_result)

        # Save the contract
        save_contract_result = save_contract(project_name, contract)
        print("Save Contract Result:", save_contract_result)
        if not get_user_confirmation("Do you want to proceed with test generation?"):
            return

        # Step 3: Generate tests
        test_result = smart_contract_crews.test_generation_crew(contract).kickoff()
        print("Test Generation Result:", test_result)
        if not get_user_confirmation("Do you want to proceed with saving the tests?"):
            return

        # Save the tests
        save_tests_result = save_tests(project_name, str(test_result))
        print("Save Tests Result:", save_tests_result)
        if not get_user_confirmation("Do you want to proceed with contract validation?"):
            return

        # Step 4: Validate the contract and tests
        validation_result = smart_contract_crews.contract_validation_crew(contract).kickoff()
        print("Contract Validation Result:", validation_result)

        test_validation_result = smart_contract_crews.test_validation_crew(str(test_result)).kickoff()
        print("Test Validation Result:", test_validation_result)
        if not get_user_confirmation("Do you want to proceed with frontend design?"):
            return

        # Step 5: Design Frontend
        frontend_result = frontend_crews.frontend_design_crew(frontend_requirements).kickoff()
        print("Frontend Design Result:", frontend_result)
        if not get_user_confirmation("Do you want to proceed with JavaScript implementation?"):
            return

        # Extract the HTML content from the frontend_result
        html_content = str(frontend_result)

        # We'll assume the CSS is included in the HTML file via a CDN
        css_content = "/* Tailwind CSS is loaded from CDN */"

        # Step 6: Implement JavaScript
        js_result = frontend_crews.javascript_implementation_crew(html_content).kickoff()
        print("JavaScript Implementation Result:", js_result)
        if not get_user_confirmation("Do you want to proceed with Stacks.js integration?"):
            return

        # Update js_content with the implementation result
        js_content = str(js_result)

        # Step 7: Integrate Stacks.js
        stacksjs_result = frontend_crews.stacksjs_integration_crew(js_content).kickoff()
        print("Stacks.js Integration Result:", stacksjs_result)
        if not get_user_confirmation("Do you want to proceed with smart contract integration?"):
            return

        # Keep Stacks.js integration separate
        stacksjs_content = str(stacksjs_result)

        # Step 8: Integrate Smart Contract with Frontend
        contract_integration_result = frontend_crews.contract_integration_crew(stacksjs_content, contract).kickoff()
        print("Contract Integration Result:", contract_integration_result)
        if not get_user_confirmation("Do you want to save the frontend files?"):
            return

        # Final JavaScript code with contract integration
        final_stacksjs_content = str(contract_integration_result)

        # Save the frontend files
        save_frontend_result = save_frontend(project_name, html_content, css_content, js_content, final_stacksjs_content)
        print("Frontend Save Result:", save_frontend_result)

        print(f"\nProject completed! All files have been saved in the '{project_name}' directory.")
        print(f"Smart contract: {project_name}/contracts/contract.clar")
        print(f"Tests: {project_name}/tests/contract_test.ts")
        print(f"Frontend: {project_name}/frontend/index.html")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()