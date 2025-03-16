import unittest
from myapp.repository import QuoteRepository  # Імпортуйте ваш клас репозиторію
from myapp.models import Quote  # Ваш SQLAlchemy ORM клас

class TestQuoteRepository(unittest.TestCase):
    def setUp(self):
        self.repo = QuoteRepository()
        self.test_quote = Quote(id=1, text="Test quote", author="Test Author")

    def test_add_quote(self):
        self.repo.add(self.test_quote)
        result = self.repo.get_by_id(1)
        self.assertEqual(result.text, "Test quote")

    def test_delete_quote(self):
        self.repo.add(self.test_quote)
        self.repo.delete(1)
        result = self.repo.get_by_id(1)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

