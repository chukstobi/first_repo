reg_user_file = open("reg_users.csv", "a")
try:
    print("welcome to the department predictor machine\nKindly enter details and scores for atleast 4 subjects\nInput zero for subject not offered in jamb.")
    name = input("Please input fullname: ")
    age = int(input("Age: "))
except ValueError:
    print("Kindly input age in number format.")

print()
try:
    maths_score = int(input("Please input Maths score: "))
    english_score = int(input("Please input English score: "))
    physics_score = int(input("Please input Physics score: "))
    chemistry_score = int(input("Please input Chemistry score: "))
    commerce_score = int(input("Please input Commerce score: "))
    economics_score = int(input("Please input Economics score: "))
except ValueError:
    print("Kindly input scores in number format.")
except NameError:
    print("Kindly input scores in number format.")

print()
msg_1 = "Hello " + name
msg_2 = "Below shows the departments you likely qualify."
qualified_for_engineering = maths_score >= 80 and english_score >= 70 and chemistry_score >= 70 and physics_score >= 75
qualified_for_business = maths_score >= 60 and english_score >= 70 and commerce_score >= 70 and economics_score >= 75
qualified_for_biological_sciences = maths_score >= 75 and english_score >= 80 and chemistry_score >= 70 and physics_score >= 75
qualified_for_economics = maths_score >= 60 and english_score >= 70 and commerce_score >= 70 and economics_score >= 75
print()
print(name, age, msg_1, msg_2, qualified_for_engineering, qualified_for_business, qualified_for_biological_sciences, qualified_for_economics, sep = "\n")
print(name, age, msg_1, msg_2, qualified_for_engineering, qualified_for_business, qualified_for_biological_sciences, qualified_for_economics, sep = ",", file = reg_user_file)