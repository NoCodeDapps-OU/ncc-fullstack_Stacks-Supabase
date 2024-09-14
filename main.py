import os
from dotenv import load_dotenv
from src.crews import SmartContractCrews, FrontendCrews
from src.logger import log_step

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
    os.environ["PROJECT_NAME"] = project_name
    contract_requirements = input("Describe the requirements for your smart contract: ")
    frontend_requirements = input("Describe the requirements for your frontend: ")

    try:
        # Step 1: Set up the project structure
        setup_result = smart_contract_crews.project_setup_crew(project_name).kickoff()
        log_step("Project Setup", setup_result)
        if not get_user_confirmation("Do you want to proceed with contract generation?"):
            return

        # Step 2: Generate the contract
        contract_result = smart_contract_crews.contract_design_crew(contract_requirements).kickoff()
        log_step("Contract Generation", contract_result)
        if not get_user_confirmation("Do you want to proceed with test generation?"):
            return

        # Step 3: Generate tests
        test_result = smart_contract_crews.test_generation_crew(str(contract_result)).kickoff()
        log_step("Test Generation", test_result)
        if not get_user_confirmation("Do you want to proceed with contract validation?"):
            return

        # Step 4: Validate the contract and tests
        validation_result = smart_contract_crews.contract_validation_crew(str(contract_result)).kickoff()
        log_step("Contract Validation", validation_result)

        test_validation_result = smart_contract_crews.test_validation_crew(str(test_result)).kickoff()
        log_step("Test Validation", test_validation_result)
        if not get_user_confirmation("Do you want to proceed with frontend design?"):
            return

        # Step 5: Design Frontend
        frontend_result = frontend_crews.frontend_design_crew(frontend_requirements).kickoff()
        log_step("Frontend Design", str(frontend_result))
        if not get_user_confirmation("Do you want to proceed with JavaScript implementation?"):
            return

        # Step 6: Implement JavaScript
        js_result = frontend_crews.javascript_implementation_crew(str(frontend_result)).kickoff()
        log_step("JavaScript Implementation", js_result)
        if not get_user_confirmation("Do you want to proceed with Stacks.js integration?"):
            return

        # Step 7: Integrate Stacks.js
        stacksjs_result = frontend_crews.stacksjs_integration_crew(str(js_result)).kickoff()
        log_step("Stacks.js Integration", stacksjs_result)
        if not get_user_confirmation("Do you want to proceed with smart contract integration?"):
            return

        # Step 8: Integrate Smart Contract with Frontend
        contract_integration_result = frontend_crews.contract_integration_crew(str(stacksjs_result), str(contract_result)).kickoff()
        log_step("Contract Integration", contract_integration_result)

        print(f"\nProject completed! All steps have been logged in the '{project_name}/logs/generation_log.txt' file.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        log_step("Error", str(e))

if __name__ == "__main__":
    main()