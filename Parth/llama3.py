from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from speak import speak
import os
from apiKey import repo_id_2, hf_token
import logging
from contextlib import redirect_stdout
import io
import re

class Mistralai_Conversation:
    def __init__(self):
        logging.getLogger().setLevel(logging.ERROR)
        os.environ['HF_Token'] = hf_token
        self.llm = HuggingFaceEndpoint(repo_id=repo_id_2, max_length=2048, temperature=0.7, token=hf_token)
        self.conversation_history = []

    def Mistral(self, quest):
        template = """Conversation so far:
        {history}
        User: {question}
        Assistant: Let's think step by step."""
        prompt = PromptTemplate(template=template, input_variables=["history", "question"])
        self.conversation_history.append(f"User: {quest}")
        history_text = "\n".join(self.conversation_history)
        pipeline = RunnableSequence(prompt, self.llm)
        f = io.StringIO()
        with redirect_stdout(f):
            result = pipeline.invoke({"history": history_text, "question": quest})
        self.conversation_history.append(f"Assistant: {result}")
        
        # Save the response with the question's name
        safe_filename = re.sub(r'[^a-zA-Z0-9]', '_', quest)  # Remove special characters for safe filenames
        with open(f"{safe_filename}.txt", "w") as file:
            file.write(result)

        with open("conversation_log.txt", "a") as file:
            file.write(f"User: {quest}\nAssistant: {result}\n\n")

        # Check if response contains code and prevent speaking it
        if not re.search(r'```[a-zA-Z]*\n.*\n```', result, re.DOTALL):
            speak(result)

        # Always display the result
        print(result)
        return result

class Mistralai:
    def Mistral(self,quest):
        logging.getLogger().setLevel(logging.ERROR)

        os.environ['HF_Token'] = hf_token

        llm = HuggingFaceEndpoint(repo_id=repo_id_2, max_length = 2048 , temperature=0.7, token=hf_token)

        question = quest
        template = """Question: {question}
        Answer: Let's think step by step."""
        prompt = PromptTemplate(template=template, input_variables=["question"])

        pipeline = RunnableSequence(
        prompt,llm)

        f = io.StringIO()
        with redirect_stdout(f):
            result = pipeline.invoke({"question": question})
        #^ saves the resopnse whith the name of question
        with open(f"{question}.txt","w") as file:
            file.write(result)
            file.close()
        speak(result)