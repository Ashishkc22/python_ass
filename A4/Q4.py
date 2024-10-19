

skills_A = {'Python', 'Java', 'SQL'}
skills_B = {'Python', 'HTML', 'CSS'}


common_skills = skills_A.intersection(skills_B)
print("\nSkills in both sets:", common_skills)

unique_skills_A = skills_A.difference(skills_B)
print("Skills unique to A:", unique_skills_A)

all_skills = skills_A.union(skills_B)
print("Union of both skill sets:", all_skills)
