# main.py

from agents.gemini_agent import create_gemini_agent

def main():
    agent = create_gemini_agent()
    
    # Sample Query 1: Ask about ROI for a specific campaign
    query1 = "What is the ROI for Campaign 1?"
    response1 = agent.run(query1)
    print("Response to Query 1:")
    print(response1)
    
    # Sample Query 2: Ask about Conversion Rate for Email campaigns
    query2 = "Tell me the conversion rate for Email campaigns."
    response2 = agent.run(query2)
    print("Response to Query 2:")
    print(response2)

if __name__ == "__main__":
    main()
