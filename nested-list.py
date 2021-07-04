records = []
sec_low_grades = []
scores = set()

for i in range(int(input())):
  name = input()
  score = float(input())
  records.append([name, score])
  scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in records:
  if score == second_lowest:
    sec_low_grades.append(name)

for name in sorted(sec_low_grades):
  print(name, end='\n')
