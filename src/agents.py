from crewai import Agent
from anthropic import Anthropic
from langchain_anthropic import ChatAnthropic

from .tools import (
    ClarityProjectSetup,
    ClarityContractGenerator,
    ClarityTestGenerator,
    ContractValidator,
    ProjectFinalizer,
    TestValidator,
    FrontendTools,
    StacksTools,
    ContractIntegrationTools
)

class SmartContractAgents:
    def __init__(self, model="claude-3-opus-20240229"):
        self.model = model
        self.llm = ChatAnthropic(model=self.model)

    def project_setup_agent(self):
        return Agent(
            role='Clarity Project Manager',
            goal='Set up a new Clarity smart contract project structure',
            backstory='You are an experienced blockchain project manager specializing in Clarity smart contract development.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[ClarityProjectSetup.setup_project]
        )

    def contract_designer(self):
        return Agent(
            role='Smart Contract Designer',
            goal='Design and implement Clarity smart contracts based on user requirements',
            backstory='You are an expert Clarity developer with years of experience in designing secure and efficient smart contracts.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[ClarityContractGenerator.generate_contract]
        )

    def contract_tester(self):
        return Agent(
            role='Smart Contract Tester',
            goal='Create comprehensive test suites for Clarity smart contracts',
            backstory='You are a meticulous QA engineer specializing in blockchain technology and smart contract testing. Your expertise lies in crafting thorough test suites that cover all aspects of Clarity smart contracts, including edge cases and potential vulnerabilities.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[ClarityTestGenerator.generate_tests]
        )

    def contract_validator(self):
        return Agent(
            role='Contract Validator',
            goal='Validate Clarity smart contracts for correctness and security',
            backstory='You are an expert in Clarity smart contract validation, responsible for ensuring contracts meet all security and functionality requirements.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[ContractValidator.validate_contract]
        )
    
    def test_validator(self):
        return Agent(
            role='Test Validator',
            goal='Validate and ensure the completeness of Clarity smart contract test suites',
            backstory='You are an expert in Clarity smart contract testing, responsible for validating test suites and ensuring they cover all aspects of the contract.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[TestValidator.validate_tests]
        )

    def project_finalizer(self):
        return Agent(
            role='Project Finalizer',
            goal='Validate and finalize the Clarity smart contract project',
            backstory='You are a senior blockchain architect responsible for ensuring the quality and completeness of Clarity smart contract projects.',
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
            tools=[
                ContractValidator.validate_contract,
                TestValidator.validate_tests,
                ProjectFinalizer.finalize_project
            ]
        )

class FrontendAgents:
    def __init__(self, model="claude-3-opus-20240229"):
        self.model = model
        self.llm = ChatAnthropic(model=self.model)

    def frontend_designer(self):
        return Agent(
            role='Frontend Designer',
            goal='Design and implement the frontend structure using HTML and Tailwind CSS',
            backstory='You are an expert frontend designer with years of experience in creating beautiful and responsive web interfaces.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[FrontendTools.generate_html_css]
        )

    def javascript_developer(self):
        return Agent(
            role='JavaScript Developer',
            goal='Implement frontend functionality using JavaScript',
            backstory='You are a skilled JavaScript developer with expertise in creating interactive and dynamic web applications.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[FrontendTools.generate_javascript]
        )

    def stacksjs_integrator(self):
        return Agent(
            role='Stacks.js Integrator',
            goal='Integrate Stacks.js components into the frontend',
            backstory='You are an expert in blockchain technology and Stacks.js integration, with a deep understanding of connecting frontends to blockchain functionality.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[StacksTools.integrate_stacksjs]
        )

    def contract_integrator(self):
        return Agent(
            role='Smart Contract Integrator',
            goal='Integrate the Clarity smart contract with the frontend',
            backstory='You are a blockchain developer specializing in connecting smart contracts to frontend applications, ensuring seamless interaction between the UI and the blockchain.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[ContractIntegrationTools.integrate_contract]
        )