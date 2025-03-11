import unittest
from app.repository import get_contact_by_id

class TestRepository(unittest.TestCase):
    def test_get_contact_by_id(self):
        contact = get_contact_by_id(1)
        self.assertIsNotNone(contact)
        self.assertEqual(contact.id, 1)

if __name__ == '__main__':
    unittest.main()
