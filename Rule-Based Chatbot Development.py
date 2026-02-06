#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


def get_library_response(user_input):
    # Standardize input [cite: 31]
    text = user_input.lower().strip()
    
    # 1. Exit Conditions [cite: 33]
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for visiting the Library. Happy reading!"

    # 2. Greetings [cite: 36]
    if re.search(r"\b(hello|hi|hey|greetings)\b", text):
        return "Hello! Welcome to the Library Assistant. How can I help you today?"

    # 3. Book Categories (Similar to Account Types [cite: 38])
    if re.search(r"\b(categories|genres|types of books|collection)\b", text):
        return "We have Fiction, Non-Fiction, Sci-Fi, Biography, and Academic journals."

    # 4. Membership/Registration (Similar to Open Account [cite: 60])
    if re.search(r"\b(membership|register|join|new card|sign up)\b", text):
        return "To get a library card, please bring a valid ID and proof of residence to the front desk."

    # 5. Library Timings (Similar to Branch Timings [cite: 49])
    if re.search(r"\b(hours|timing|open|close|work hours)\b", text):
        return "The library is open from 8:00 AM to 8:00 PM (Mon-Sat) and 10:00 AM to 4:00 PM on Sundays."

    # 6. Borrowing Rules/Loans (Similar to Loans [cite: 63])
    if re.search(r"\b(borrow|return|loan|due date|days)\b", text):
        return "You can borrow up to 5 books for 14 days. Renewals can be done online."

    # 7. Fine/Late Fees (Similar to Interest Rates [cite: 71])
    if re.search(r"\b(fine|late fee|charges|penalty)\b", text):
        return "Late returns incur a fine of $0.50 per day per book."

    # 8. Default Fallback [cite: 85]
    return "I'm sorry, I don't understand that. You can ask about: timings, membership, book categories, or borrowing rules."


# In[3]:


def run_library_chatbot():
    print("LibraryBot: Welcome! I am your rule-based library assistant.")
    print("LibraryBot: Type 'exit' or 'bye' to leave.\n")
    
    while True:
        user_text = input("You: ")
        
        # Get response from our logic function
        response = get_library_response(user_text)
        print(f"LibraryBot: {response}")
        
        # Stop the loop if the response is an exit message [cite: 99]
        if any(word in user_text.lower() for word in ["bye", "exit", "quit"]):
            break

# Execute the chatbot
run_library_chatbot()


# In[ ]:




