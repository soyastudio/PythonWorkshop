import ollama

response = ollama.chat(model='deepseek-r1:8b', messages=[
  {
    'role': 'user',
    'content': 'Write a Python function to sort a list.',
  },
])
print(response['message']['content'])
