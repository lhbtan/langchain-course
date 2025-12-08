from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langsmith import Client

    

client = Client()
run_id = '019afe64-b48c-78e2-8992-fa98bcd66b34'
llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)

def main():


    # Update the run status to "aborted" (equivalent to stopping it)
    client.update_run(run_id=run_id, status="aborted")
    #print("Hello from langchain-course!")
    #result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in Kuala lumpur malaysia on linkedin and list their details?")})
    #print(result)

if __name__ == "__main__":
    main()
