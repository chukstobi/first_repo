# qualified_for_engineering: 80% maths, 70% english
# qualified_for_business: 60% maths, 70% english
# qualified_for_theology: 20% maths, 80% english

maths_score = int(input("please input maths score: "))
english_score = int(input("Please input englsih score: "))

print()
print("qualified for engineering".ljust(26), ":", maths_score >= 80 and english_score >= 70)
print("qualified for busniess".ljust(26), ":", maths_score >= 60 and english_score >= 70)
print("qualified for theology".ljust(26), ":", maths_score >= 20 and english_score >= 80)