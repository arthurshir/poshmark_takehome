import sys, unittest;
from test.support import captured_stdout
from io import StringIO
from review_processing import HighlightGenerator, Review
from rh import review_highlights_from_stdin


class BasicTestReviewClass(unittest.TestCase):
  def test_basic_positive_classification(self):
    review = Review("I love this place and their sandwiches are delicious.")
    review.classify()
    self.assertTrue(review.is_positive)
    self.assertFalse(review.is_negative)

  def test_basic_negative_classification(self):
    review = Review("I hate the food and their bathroom is gross.")
    review.classify()
    self.assertTrue(review.is_negative)
    self.assertFalse(review.is_positive)

  def test_basic_regular_classification(self):
    review = Review("I come here all the time.")
    review.classify()
    self.assertTrue(review.is_regular)

  def test_basic_strong_review(self):
    review = Review("The sandwiches are consistently great here.")
    review.classify()
    review.assess_strength()
    self.assertEqual(review.strength, 1)


class BasicTestHighlightGeneratorClass(unittest.TestCase):
  def test_top_review(self):
    reviews = ["I come here sometimes", "We ordered falafel", "I like tomatoes", "The sandwiches are consistently great here."]

    highlightGenerator = HighlightGenerator(reviews)
    highlightGenerator.process_reviews()
    sorted_reviews = highlightGenerator.reviews
    top_review = sorted_reviews[0]
    
    self.assertEqual(top_review.text, "The sandwiches are consistently great here.")

class BasicTestRHScript(unittest.TestCase):
  def test_top_review(self):
    sys.argv = ["_", "test_reviews.txt", "1"]
    with captured_stdout() as stdout:
        review_highlights_from_stdin()
    self.assertEqual(stdout.getvalue(), "The sandwiches are consistently great here.\n")

if __name__ == '__main__':
  unittest.main()
