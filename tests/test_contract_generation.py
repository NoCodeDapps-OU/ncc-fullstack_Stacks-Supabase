import unittest
from src.utils.clarity_helpers import generate_clarity_contract, validate_clarity_contract

class TestContractGeneration(unittest.TestCase):
    def test_contract_generation(self):
        requirements = "A simple token contract with mint and transfer functions"
        contract = generate_clarity_contract(requirements)
        self.assertIsNotNone(contract)
        self.assertIn("define-fungible-token", contract)
        self.assertIn("define-public (mint", contract)
        self.assertIn("define-public (transfer", contract)

    def test_contract_validation(self):
        valid_contract = """
(define-fungible-token my-token)

(define-public (mint (amount uint) (recipient principal))
    (ft-mint? my-token amount recipient)
)

(define-public (transfer (amount uint) (sender principal) (recipient principal))
    (ft-transfer? my-token amount sender recipient)
)
"""
        validation_result = validate_clarity_contract(valid_contract)
        self.assertEqual(validation_result, "Contract is valid.")

if __name__ == '__main__':
    unittest.main()