scores = [51, 71, 76, 81, 46, 67, 58]
total_score = sum(scores)
average_score = total_score / len(scores)
pass_rate = len([x for x in scores if x >= 60]) / len(scores) * 100
print(f"总分: {total_score}")
print(f"平均分: {average_score:.2f}")
print(f"及格率: {pass_rate:.2f}%")
