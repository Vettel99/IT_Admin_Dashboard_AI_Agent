import os
import asyncio
from dotenv import load_dotenv
from browser_use_sdk.v3 import AsyncBrowserUse

load_dotenv()

async def run_it_automation():
    if not os.getenv("BROWSER_USE_API_KEY"):
        raise ValueError("Please set BROWSER_USE_API_KEY in your .env file")

    client = AsyncBrowserUse()
    TARGET_URL = "https://your-ngrok-url.app" # Ensure this matches your Ngrok URL
    
    task_prompt = f"""
    You are an IT Support Agent. Go to the IT admin dashboard at {TARGET_URL}.
    
    Task 1: Check the dashboard table to see if a user with the email 'sarah@company.com' exists. 
    If she DOES NOT exist, navigate to the 'Create User' page and create an account for her with the name 'Sarah Connor' and role 'Admin'. 
    If she DOES exist, skip the creation step.
    
    Task 2: Navigate to the 'Reset Password' page and reset the password for 'john@company.com'.
    """

    print("Deploying Browser-Use Agent to the cloud...")
    
    # In v3, client.run() returns an asynchronous iterator for streaming messages
    run = client.run(task_prompt)
    
    async for msg in run:
        print(f"[{msg.role}] {msg.summary}")
        
    # The final output is available on the result object after the iterator finishes
    print("\n✅ Execution Output:")
    print(run.result.output)

if __name__ == "__main__":
    asyncio.run(run_it_automation())