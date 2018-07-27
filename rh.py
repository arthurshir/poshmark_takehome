import sys
from review_processing import HighlightGenerator, Review

def review_highlights_from_stdin():
  if len(sys.argv) >= 3:
    # Get arvg
    reviews_txt_name = sys.argv[1]
    number_of_highlights = int(sys.argv[2])

    # Open reviews and print result
    reviews_file = open(reviews_txt_name)
    review_texts = reviews_file.read().split('\n')
    print("\n".join(review_highlights(review_texts, number_of_highlights)))
    reviews_file.close()
  else:
      print ("Insufficient commands")

def review_highlights(reviews, max):
  # Initialize highlight generator and process reviews
  highlightGenerator = HighlightGenerator(reviews)
  highlightGenerator.process_reviews()
  sorted_reviews = highlightGenerator.reviews

  # Return review texts
  output_reviews = sorted_reviews[:min(len(sorted_reviews), max)]
  return [review.text for review in output_reviews]

if __name__ == '__main__':
  review_highlights_from_stdin()
