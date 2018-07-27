# Poshmark Takehome
**Author**: Arthur Shir

**Development Duration**: 7/26/18, 2:45PM - 5:05PM

## Problem Description

Extract highlights from yelp competitor reviews.

## Requirements

Requires Python 3.0+. No other installation is needed.

## Run Commands

Run unit tests
```
  python rh_unittests.py
```

Get highlights
```
  python rh.py test_reviews.txt 2
```

## Python Standard Libraries Used

- sys
- unittest
- test.support.captured_stdout
- io.StringIO
- functools.reduce


## Overall Highlights Strategy

Algorithm:
1. Classify each review (Can have multiple classes). [Time Complexity: O(|reviews| * |review| * |list_of_words|)]
2. Calculate review highlight strength. [Time Complexity: O(n^2)]
3. Return sorted reviews. [Time Complexity: O(nlogn)]


### 1. Use phrase search to classify reviews:

  - Positive phrase types:
    - good customer service
    - good food (Must be very positive)
    - popular

  - Critical phrase types:
    - Rude customer service
    - Dirty restaraunt
    - Bad food

  - Phrases that indicate a regular:
    - Indicates often or repeated customer

### 2. Measure review highlight strength

- Top tier: Positive or negative review by a regular.
- 2nd Tier: Positive or negative review.
- 3rd Tier: Review by a regular.
- 4th Tier: No notable classification.

### 3. Return sorted Reviews
Return n highest rated reviews.


## What I would improve with more time:
- Replace classification algorithm with some kind of preprocessing or optimization.
- Put into classification text files into CSV form.
  - Explore more into further subclassing of phrase types.
- Revise classification text files.
- Try different methods of review highlight strength.
- Utilize machine learning to create models of helpful reviews.
- Web scraper of professional food reviews to find professional grade reviews.
- Code review to meet modern Python best practices.