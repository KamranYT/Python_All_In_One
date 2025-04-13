import streamlit as st
import random

# Add this at the beginning of your main.py file
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff; /* Light blue background */
        color: #333; /* Dark text color */
    }
    .stButton {
        background-color: #4CAF50; /* Green background for buttons */
        color: white; /* White text */
        border: none; /* No border */
        padding: 10px 20px; /* Padding */
        text-align: center; /* Center text */
        text-decoration: none; /* No underline */
        display: inline-block; /* Inline block */
        font-size: 16px; /* Font size */
        margin: 4px 2px; /* Margin */
        cursor: pointer; /* Pointer cursor */
        border-radius: 5px; /* Rounded corners */
    }
    .stButton:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stRadio {
        margin: 10px 0; /* Margin for radio buttons */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Quiz Questions
questions = [
    {
        "question": "What is the output of the following?\n\n```python\nx = 10\ndef foo():\n    print(x)\n    x = 5\nfoo()\n```",
        "options": ["10", "5", "UnboundLocalError", "NameError"],
        "answer": "UnboundLocalError",
        "explanation": "Python treats 'x' as a local variable inside foo, so it raises UnboundLocalError.",
    },
    {
        "question": "What does this expression return?\n\n```python\nbool('False')\n```",
        "options": ["False", "True", "'False'", "Error"],
        "answer": "True",
        "explanation": "Non-empty strings are truthy in Python, even if the content is 'False'.",
    },
    {
        "question": "What is the result of 3 < 2 < 1?",
        "options": ["True", "False", "Error", "Depends on interpreter"],
        "answer": "False",
        "explanation": "Chained comparisons in Python are evaluated as 3 < 2 and 2 < 1, both must be True.",
    },
    {
        "question": "What does this print?\n\n```python\na = (1, 2, [3, 4])\na[2][0] = 99\nprint(a)\n```",
        "options": ["(1, 2, [3, 4])", "(1, 2, [99, 4])", "Error", "(1, 2, 3, 4)"],
        "answer": "(1, 2, [99, 4])",
        "explanation": "Tuples are immutable, but mutable elements inside them (like lists) can be changed.",
    },
    {
        "question": "What will happen?\n\n```python\nprint({True: 'yes', 1: 'no', 1.0: 'maybe'})\n```",
        "options": [
            "All keys will be printed",
            "Last value overrides previous ones",
            "KeyError",
            "Duplicate keys allowed",
        ],
        "answer": "Last value overrides previous ones",
        "explanation": "True, 1, and 1.0 all hash to the same value; latest value overrides.",
    },
    {
        "question": "Which of the following is not a valid Python data structure?",
        "options": ["Stack", "Set", "Dictionary", "List"],
        "answer": "Stack",
        "explanation": "Python does not have a built-in 'Stack' type, but it can be implemented using lists.",
    },
    {
        "question": "What's the output?\n\n```python\nprint([i for i in range(3)])\nprint((i for i in range(3)))\n```",
        "options": [
            "[0,1,2] and [0,1,2]",
            "Generator object",
            "Error",
            "[0,1,2] and generator object",
        ],
        "answer": "[0,1,2] and generator object",
        "explanation": "List comprehension creates a list; generator expression returns a generator object.",
    },
    {
        "question": "What's the purpose of nonlocal in nested functions?",
        "options": [
            "Declare a global variable",
            "Declare variable as non-editable",
            "Modify outer enclosing scope variable",
            "Avoid recursion",
        ],
        "answer": "Modify outer enclosing scope variable",
        "explanation": "'nonlocal' allows you to assign to variables in the nearest enclosing scope that's not global.",
    },
    {
        "question": 'What is output of this code?\n\n```python\ndef foo(bar=[]):\n    bar.append("baz")\n    return bar\n\nprint(foo())\nprint(foo())\n```',
        "options": [
            "['baz'] then ['baz']",
            "['baz'] then ['baz', 'baz']",
            "[] then []",
            "Error",
        ],
        "answer": "['baz'] then ['baz', 'baz']",
        "explanation": "Default mutable arguments persist across function calls.",
    },
    {
        "question": "How do Python's is and == differ?",
        "options": [
            "is checks for content equality",
            "== checks for memory address",
            "is checks for identity, == checks for equality",
            "They are the same",
        ],
        "answer": "is checks for identity, == checks for equality",
        "explanation": "'is' checks memory location, '==' checks value.",
    },
    {
        "question": "What does __slots__ do in Python classes?",
        "options": [
            "Automatically generates init",
            "Limits attributes to save memory",
            "Enables static typing",
            "Allows dynamic attributes",
        ],
        "answer": "Limits attributes to save memory",
        "explanation": "__slots__ prevents creation of __dict__, saving memory in large number of instances.",
    },
    {
        "question": "What's the purpose of the with statement in Python?",
        "options": ["Looping", "Scoping", "Resource management", "Error handling"],
        "answer": "Resource management",
        "explanation": "'with' ensures proper acquisition and release of resources like files or locks.",
    },
    {
        "question": "What is output of this code?\n\n```python\nprint(0.1 + 0.2 == 0.3)\n```",
        "options": ["True", "False", "Error", "None"],
        "answer": "False",
        "explanation": "Floating point arithmetic can lead to small precision errors.",
    },
    {
        "question": "What will this code output?\n\n```python\ndef func(val, lst=[]):\n    lst.append(val)\n    return lst\n\nprint(func(1))\nprint(func(2))\n```",
        "options": ["[1] [2]", "[1] [1, 2]", "Error", "[1, 2] [1, 2]"],
        "answer": "[1] [1, 2]",
        "explanation": "Default list argument keeps state across function calls.",
    },
    {
        "question": "What's the result of list('abc') * 2?",
        "options": [
            "'abcabc'",
            "['a', 'b', 'c', 'a', 'b', 'c']",
            "['abc', 'abc']",
            "Error",
        ],
        "answer": "['a', 'b', 'c', 'a', 'b', 'c']",
        "explanation": "The list is duplicated, not joined as a string.",
    },
    {
        "question": "Which method ensures thread-safety in Python multithreading?",
        "options": ["Lock.acquire()", "with Lock()", "join()", "All of the above"],
        "answer": "All of the above",
        "explanation": "Each is part of safe threading practices depending on the situation.",
    },
    {
        "question": "What does enumerate() return?",
        "options": ["Index", "Index + value", "List of values", "Key-value pairs"],
        "answer": "Index + value",
        "explanation": "enumerate() returns an iterator of index and value pairs.",
    },
    {
        "question": "What is the result of type(lambda x: x)?",
        "options": ["function", "lambda", "<class 'function'>", "<lambda object>"],
        "answer": "<class 'function'>",
        "explanation": "Lambda expressions create function objects of type 'function'.",
    },
    {
        "question": "What is the MRO (Method Resolution Order) in Python?",
        "options": [
            "Compilation order",
            "Order of inheritance lookup",
            "Recursion order",
            "Loop optimization",
        ],
        "answer": "Order of inheritance lookup",
        "explanation": "MRO determines how base classes are searched when calling a method.",
    },
    {
        "question": "What does the walrus operator (:=) do in Python?",
        "options": [
            "Compare variables",
            "Assign values in expressions",
            "Loop through lists",
            "Return None",
        ],
        "answer": "Assign values in expressions",
        "explanation": "The walrus operator allows assignment inside expressions like loops or conditions.",
    },
]

random.shuffle(questions)

# App State
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.show_result = False
    st.session_state.name = ""

st.title("🧠 Advanced Python Quiz")

# User name input
if not st.session_state.name:
    st.session_state.name = st.text_input("Enter your name to begin:", "")
    st.stop()

# Quiz Logic
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.subheader(f"Question {st.session_state.current_q + 1}")
    st.markdown(q["question"])

    choice = st.radio("Choose one:", q["options"], key=st.session_state.current_q)

    if st.button("Submit"):
        if choice == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrect!")
        st.info(f"**Explanation**: {q['explanation']}")
        st.session_state.current_q += 1
        st.rerun()
else:
    st.session_state.show_result = True

# Final Result
if st.session_state.show_result:
    st.title("🎉 Quiz Completed!")
    st.markdown(f"### 👤 Name: {st.session_state.name}")
    st.markdown(f"### 🧾 Final Score: {st.session_state.score} / {len(questions)}")
    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
