"""
Scores To Rating Function Design
Let's work through building up the structure of a new function. Imagine that you work for a consumer ratings website. Users submit reviews and scores for products they use, and you show the results so that consumers can make informed choices.

Throughout this section we will write a function that takes as input five scores and aggregates them to output a single rating.

Because the highest and lowest scores might be outliers and skew the results, we will take the three middle scores out of the five, discarding the highest and lowest.

Then we will take the average (mean) of those three middle scores.

For example, if the scores are 1,2,2,4,4 then we take the average of 2, 2 and 4 to get 2.6666666666.

Then we will map that average score to a written rating like this:

Average Score	Rating
0 <= score < 1	Terrible
1 <= score < 2	Bad
2 <= score < 3	OK
3 <= score < 4	Good
4 <= score <= 5	Excellent
"""
def convert_to_numeric(score):
    """
    Convert the score to a float.
    """
    converted_score = float(score)
    return converted_score

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """
    Find the sum of the middle three numbers out of the five given.
    """
    max_score = max(score1,score2,score3,score4,score5)
    min_score = min(score1,score2,score3,score4,score5)
    sum = score1 + score2 + score3 + score4 + score5 - max_score - min_score
    return sum


def score_to_rating_string(av_score):
    """
    Convert the average score, which should be between 0 and 5, 
    into a rating.
    """
    if av_score < 1:
        rating = "Terrible"
    elif av_score < 2:
        rating = "Bad"
    elif av_score < 3:
        rating = "OK"
    elif av_score < 4:
        rating = "Good"
    else:          #Using else at the end, every possible case gets caught
        rating = "Excellent"
    return rating


def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


print(scores_to_rating(1, 2, 2, 4, 4))
print(scores_to_rating(2, 2, 2, 2, 5))
print(scores_to_rating(4, 3, 2, 5, 2))
print(scores_to_rating(6, 2, 2, 1, 3))
print(scores_to_rating(2, 1, 2, 3, 2))
print(scores_to_rating(1, 5, 2, 4, 4))
