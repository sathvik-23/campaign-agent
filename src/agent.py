# src/agent.py
import json
import os
from gemini import get_analysis

def run_agent():
    # Load dataset.json from the project root
    dataset_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset.json')
    with open(dataset_path, 'r', encoding='utf-8') as f:
        campaigns = json.load(f)
    
    # Process each campaign record
    for campaign in campaigns:
        print(f"\nProcessing Campaign ID {campaign['Campaign_ID']} for {campaign['Company']}")
        prompt = (
            f"Analyze the following campaign details and provide insights on performance, targeting, "
            f"and optimization opportunities:\n"
            f"Company: {campaign['Company']}\n"
            f"Campaign Type: {campaign['Campaign_Type']}\n"
            f"Target Audience: {campaign['Target_Audience']}\n"
            f"Duration: {campaign['Duration']}\n"
            f"Channel Used: {campaign['Channel_Used']}\n"
            f"Conversion Rate: {campaign['Conversion_Rate']}\n"
            f"Acquisition Cost: {campaign['Acquisition_Cost']}\n"
            f"ROI: {campaign['ROI']}\n"
            f"Location: {campaign['Location']}\n"
            f"Language: {campaign['Language']}\n"
            f"Clicks: {campaign['Clicks']}\n"
            f"Impressions: {campaign['Impressions']}\n"
            f"Engagement Score: {campaign['Engagement_Score']}\n"
            f"Customer Segment: {campaign['Customer_Segment']}\n"
            f"Date: {campaign['Date']}"
        )
        try:
            analysis = get_analysis(prompt)
            print(f"Analysis: {analysis}")
        except Exception as e:
            print(f"Error processing Campaign ID {campaign['Campaign_ID']}: {str(e)}")
