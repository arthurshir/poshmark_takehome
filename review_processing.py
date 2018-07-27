from functools import reduce

regulars_words = open("classification_text_files/regulars_words.txt").read().split('\n')
positive_words = open("classification_text_files/positive_words.txt").read().split('\n')
negative_words = open("classification_text_files/negative_words.txt").read().split('\n')

class HighlightGenerator:

  def __init__(self, review_texts):
    # Clean and process reviews
    self.review_texts = reduce(lambda x, y: x + y, [text.split('.') for text in review_texts])
    self.review_texts = [text.strip() for text in self.review_texts]
    self.review_texts = [text for text in self.review_texts if len(text) > 2]
    self.reviews = []

  def process_reviews(self):
    for text in self.review_texts:
      review = Review(text + ".")
      review.classify()
      review.assess_strength()
      self.reviews.append(review)
    self.reviews.sort(key = lambda x: x.strength, reverse=True)

  # Return reviews sorted by highlight relevency.
  def get_reviews(self):
    return self.reviews


class Review:

  def __init__(self, text):
    self.text = text
    self.is_regular = False
    self.is_positive = False
    self.is_negative = False
    self.strength = 0

  # Note: Replace this implementation with some kind of preprocessing or optimization
  #   - Performance: O(|reviews| * |review| * |list_of_words|)
  def classify(self):
    self.is_regular = any(word in self.text for word in regulars_words)
    self.is_positive = any(word in self.text for word in positive_words)
    self.is_negative = any(word in self.text for word in negative_words)

  # Rating description:
  # - Top tier: regular + negative or positive
  # - 2nd Tier: positive or negative
  # - 3rd Tier: regular
  # - 4th Tier: no notable classification
  def assess_strength(self):
    if (self.is_regular and self.is_positive) or (self.is_regular and self.is_negative):
      self.strength = 1.0
    elif self.is_positive or self.is_negative:
      self.strength = 0.5
    elif self.is_regular:
      self.strength = 0.25

  def __str__(self):
    return "[review] class: {}{}{}, text: {}".format(\
      "r" if self.is_regular else "",\
      "p" if self.is_positive else "",\
      "n" if self.is_negative else "",\
      self.text \
      )
