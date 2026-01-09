from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_ollama import ChatOllama

@tool
def multiply(a: int, b: int) ->int:
    "Multiply two numbers together"""
    return a*b

@tool
def add(a: int, b: int) ->int:
    "Add two numbers together"""
    return a+b

llm =  ChatOllama (model="llama3.2:latest")

llm_with_tools = llm.bind_tools([multiply, add])
human_message = HumanMessage(content="What is 4+5")
# if the prompt was "what is 4+5", suggest tool call add only
# if the prompt was "what is 4*5", suggest tool call multiply only
# if the prompt was "what is 4+5 and 4*5", suggest tool call add and multiply

ai_message = llm_with_tools.invoke([human_message]) # tool, response.
print(ai_message)

# Now, we dont  invoke the tool from manual.
# tool_message = multiply.invoke(ai_message.tool_calls[0])

tool_messages = []
for tool_call in ai_message.tool_calls:
    print("Tool call: ", tool_call)
    if tool_call['name'] == 'multiply':
        tool_result = multiply.invoke(tool_call['args'])
    elif tool_call['name'] == 'add':
        tool_result = add.invoke(tool_call['args'])
    print("Tool message: ", tool_result)
    
    # Wrap the tool result in a ToolMessage with the tool call ID
    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call['id']
    )
    tool_messages.append(tool_message)


message = [human_message, ai_message] + tool_messages
print(llm_with_tools.invoke(message).content)