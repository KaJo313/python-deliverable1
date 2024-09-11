# Step 1: Prompt the golfer for their name
golfer_name = input("Welcome to GC mini golf! What is your name? ")

# Step 2: Prompt the user to select 3- or 6- holes of mini golf
holes_played = int(input(f"Hi {golfer_name}! Would you like to play 3 or 6 holes today? "))

# Step 3: For Loop: Prompt the user to enter their hole_score for each hole;
hole_scores =[]   #list of scores for each hole
for i in range(holes_played):
    hole_scores.append(int(input(f"How many putts for hole {i+1}? (par is 3) ")))

# Step 4: Determine course par and compare against total hole scores for results
if holes_played == 3:
    course_par = 9
else:
    course_par = 18

total_score = sum(hole_scores) - course_par
if total_score > 0:
    print(f"Nice try, {golfer_name}... Your total score was: +{total_score}.")
elif total_score < 0:
    print(f"Great job, {golfer_name}! Your total score was: {total_score}.")
else:
    print(f"Good game, {golfer_name}. Your total score was: {total_score}.")

