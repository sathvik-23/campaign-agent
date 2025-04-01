import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Gemini API credentials are not set in the .env file")
    exit(1)

# Initialize Gemini API
genai.configure(api_key=API_KEY)

# Load dataset
script_dir = os.path.abspath(os.path.dirname(__file__))  # Ensure compatibility
dataset_path = os.path.join(script_dir, "../dataset.json")

if not os.path.exists(dataset_path):
    print(f"❌ Dataset file not found at {dataset_path}. Check the path.")
    exit(1)

with open(dataset_path, "r") as file:
    campaigns = json.load(file)

print("✅ Dataset Loaded Successfully!")
print(f"📊 Total campaigns in dataset: {len(campaigns)}")
print("🚀 Running Campaign Analysis (First 200 campaigns)...")

# Function to analyze campaign data with Gemini API
def analyze_campaign(campaign):
    prompt = f"""
    Analyze the following marketing campaign data and provide insights:

    - Company: {campaign["Company"]}
    - Campaign Type: {campaign["Campaign_Type"]}
    - Target Audience: {campaign["Target_Audience"]}
    - Duration: {campaign["Duration"]}
    - Channel Used: {campaign["Channel_Used"]}
    - Conversion Rate: {campaign["Conversion_Rate"]}
    - Acquisition Cost: {campaign["Acquisition_Cost"]}
    - ROI: {campaign["ROI"]}
    - Location: {campaign["Location"]}
    - Language: {campaign["Language"]}
    - Clicks: {campaign["Clicks"]}
    - Impressions: {campaign["Impressions"]}
    - Engagement Score: {campaign["Engagement_Score"]}
    - Customer Segment: {campaign["Customer_Segment"]}
    - Date: {campaign["Date"]}

    Provide insights on:
    - The effectiveness of this campaign.
    - Suggestions for improving performance.
    - Whether this campaign was cost-effective based on ROI.
    """

    try:
        model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")
        response = model.generate_content(prompt)

        # Extract response text safely
        if response and response.candidates:
            return response.candidates[0].content  # Ensure we get the right response
        else:
            return "⚠️ No response received from Gemini API."
    except genai.APIError as e:
        return f"🚨 Gemini API Error: {str(e)}"
    except Exception as e:
        return f"❌ Error analyzing campaign: {str(e)}"

# Process the first 200 campaigns
for i, campaign in enumerate(campaigns[:200], start=1):  
    print(f"\n🔍 [{i}/200] Processing Campaign ID {campaign.get('Campaign_ID', 'Unknown')} for {campaign.get('Company', 'Unknown')}...")
    analysis = analyze_campaign(campaign)
    print(analysis)

print("\n✅ Campaign Analysis Completed!")
