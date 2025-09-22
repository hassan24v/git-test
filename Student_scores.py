score = [12,18,17.5,20]

def add_score(new_score):
    score.append(new_score)
    
def average_score():
    return sum(score) / len(score)

def highest_score():
    return max(score)

add_score(19)
print("Scores:", score)
print("Averag:", average_score())
print("Highest:", highest_score())
