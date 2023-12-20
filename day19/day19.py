


def check_workflow(name, x, m, a, s):
    if name == "A":
        return True
    
    if name == "R":
        return False

    rules = workflow_dict[name].split(",")
    # print(rules)
    for rule in rules:
        if ":" in rule:
            condition, next_wf = rule.split(":")
            # print(f"check: {condition} -> {eval(condition)}")
            if eval(condition):
                return check_workflow(next_wf, x, m, a, s)

        elif rule == "A":
            return True
        elif rule == "R":
            return False 
        else:
            return check_workflow(rule, x, m, a, s)  

filename = 'input.txt'
with open (filename, 'r') as file:
    content = file.read()

workflows, ratings = content.split('\n\n')

workflow_lines = workflows.strip().split('\n')
workflow_dict = {}

for line in workflow_lines:
    key, value = line.split('{')
    value = value.rstrip('}')
    workflow_dict[key] = value


rating_lines = ratings.strip().split('\n')

sum = 0
for line in rating_lines:
    exec(line.replace(",","\n").strip("{}"))
    # print(f"x={x}, m=1{m}, a={a}, s={s}")
    accepted = check_workflow("in", x, m, a, s)
    if accepted:
        sum += x + m + a + s


print(f"Sum: {sum}")
    

