job = {
"Python": 70,
"Machine Learning": 65,
"Data Analysis": 60
}

students = [
{"name":"Student1","Python":80,"Machine Learning":70,"Data Analysis":55},
{"name":"Student2","Python":90,"Machine Learning":80,"Data Analysis":75},
{"name":"Student3","Python":60,"Machine Learning":50,"Data Analysis":40},
{"name":"Student4","Python":85,"Machine Learning":78,"Data Analysis":72},
{"name":"Student5","Python":72,"Machine Learning":69,"Data Analysis":61}
]

results = []

for student in students:
matched = 0

for skill in job:
    if student[skill] >= job[skill]:
        matched += 1

score = round((matched / len(job)) * 100, 2)

results.append((student["name"], score))

results.sort(key=lambda x: x[1], reverse=True)

for name, score in results:
print(name, "->", score, "%")
