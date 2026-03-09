import re

print("Phishing Detection Results")
print("--------------------------")

#Load sample email
with open ("phishing_samples.txt, "r") as file
           content = file.read()

# Load regex rules
with open("regex_rules.txt", "r") as file:
    rules = file.readlines()

# Scan content for matches
for rule in rules:
    rule = rule.strip()

    if re.search(rule, content, re.IGNORECASE):
        print(f"Match detected for rule: {rule}")
