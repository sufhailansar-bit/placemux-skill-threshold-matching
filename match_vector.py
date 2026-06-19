job = {
    "Python": 70,
    "Machine Learning": 65,
    "Data Analysis": 60
}

student = {
    "Python": 80,
    "Machine Learning": 70,
    "Data Analysis": 55
}

matched = 0

for skill in job:
    if student.get(skill, 0) >= job[skill]:
        matched += 1

score = round((matched / len(job)) * 100, 2)

print("Match Score:", score, "%")

if score >= 60:
    print("Eligible Candidate")
else:
    print("Not Eligible")
