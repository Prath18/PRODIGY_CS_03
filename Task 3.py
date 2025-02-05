#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

def assess_password_strength(password):
    # Define criteria
    min_length = 8
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    strength_score = 0
    if len(password) >= min_length:
        strength_score += 1
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special:
        strength_score += 1

    if strength_score == 5:
        strength = "Strong"
    elif strength_score == 4:
        strength = "Moderate"
    else:
        strength = "Weak"
        
    feedback = []
    if len(password) < min_length:
        feedback.append("Password is too short. It should be at least 8 characters.")
    if not has_uppercase:
        feedback.append("Password should contain at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password should contain at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should contain at least one number.")
    if not has_special:
        feedback.append("Password should contain at least one special character.")

   
    return {
        "password_strength": strength,
        "feedback": feedback if feedback else ["Password is strong."]
    }

password = input("Enter your password: ")
result = assess_password_strength(password)

print(f"Password Strength: {result['password_strength']}")
for advice in result['feedback']:
    print(advice)


# In[ ]:




