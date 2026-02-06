# Mini Project: Rule-Based Chatbot Development
**Theme:** Rule-Based Reasoning and Early AI Systems

## Project Objective
The objective of this assessment is to understand how early artificial intelligence systems functioned using rule-based reasoning, without relying on modern machine learning or deep learning techniques. This project simulates traditional information systems, such as FAQ-based conversational agents, used before the advent of large language models.

## Project Description
This project is a **Library Chatbot** built using a purely rule-based approach. It responds to user queries based on:
* **Predefined Rules**: Logic mapped directly to responses.
* **Keywords**: Identifying specific library-related terms.
* **Regular Expressions**: Using `re` for pattern matching without AI or NLP libraries.

## Features
The Library Chatbot can answer questions regarding:
* **Greetings**: Standard introductory interactions.
* **Membership**: How to register for a library card.
* **Book Categories**: Information on fiction, non-fiction, and other genres.
* **Timings**: Library operating hours.
* **Borrowing Rules**: Loan periods and late fee/fine information.
* **Online Reservations**: Instructions for holding books via the online portal.
* **Exit**: Closing the chat session using keywords like 'bye' or 'exit'.

## Implementation Details
The chatbot relies on a logic-flow similar to early expert systems:
1. **Input Normalization**: User input is converted to lowercase and stripped of extra spaces.
2. **Pattern Matching**: The system searches for specific regex patterns within the input.
3. **Direct Mapping**: Once a pattern is found, the system returns a predefined string response.
4. **Fallback**: A default response is provided if no rules are matched.

## Learning Outcomes
* **Understanding Rule-Based Reasoning**: Demonstrated how rules map directly to responses in a closed system.
* **Early AI Simulation**: Successfully created a conversational agent without ML or NLP models.
* **Regex Mastery**: Used regular expressions to interpret user intent in a structured way.
* **Historical AI Context**: Replicated how REAL systems like FAQ bots and IVR systems operated before modern LLMs.

## Conclusion
This project successfully demonstrates that complex tasks, such as library information management, can be handled by rule-based systems. It highlights the importance of logic-driven programming in the history of AI and provides a foundational understanding of how systems processed natural language before the modern era of deep learning.
