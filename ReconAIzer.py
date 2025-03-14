import os
import json
import subprocess
from wappalyzer import analyze
from openai import OpenAI

# Load API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please check your environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)


def get_technologies(url: str):
    """Analyze website technologies using Wappalyzer with balanced scan type."""
    results = analyze(url, scan_type='balanced')
    return list(results.get(url, {}).keys())  # Extract only technology names


def get_exploits_searchsploit(technologies: list):
    """Use SearchSploit to find local exploits related to detected technologies."""
    exploits = {}
    for tech in technologies:
        try:
            result = subprocess.run(["searchsploit", "--json", tech], capture_output=True, text=True)
            if result.stdout:
                exploits_list = json.loads(result.stdout).get("RESULTS_EXPLOIT", [])
                exploits[tech] = [exp["Title"] for exp in exploits_list[:3]]  # Store only exploit titles
            else:
                exploits[tech] = []
        except Exception as e:
            exploits[tech] = []
    return exploits


def determine_exploitable_technologies_with_ai(technologies, exploits):
    """Use AI to determine the most likely exploitable technologies dynamically, limiting data size."""
    prompt = f"""
    You are a cybersecurity AI agent specializing in bug bounty hunting. Given the following detected technologies 
    and known vulnerabilities, determine the top 3 most likely exploitable technologies.
    
    Technologies detected:
    {technologies}
    
    Known vulnerabilities:
    {json.dumps(exploits, indent=2)}
    
    Provide a concise prioritized list (only 3) of the most exploitable technologies and a brief reason.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "system", "content": "You are an expert security analyst."},
                  {"role": "user", "content": prompt}],
    )
    
    return response.choices[0].message.content


def display_exploit_summary(technologies, exploits):
    """Print a concise summary of detected technologies and exploitability."""
    print("\nhttp://dog/htb Technologies Detected:")
    for tech in technologies:
        print(f"- {tech}")
    
    print("\n Exploits Found:")
    for tech, exp in exploits.items():
        if exp:
            print(f"- {tech} ({len(exp)} exploits) - Most Critical: {exp[0]}")
    

# Main Execution
if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    print("Analyzing technologies with balanced scan...")
    detected_tech = get_technologies(target_url)
    
    print("Checking for known exploits using SearchSploit...")
    exploits_found = get_exploits_searchsploit(detected_tech)
    
    print("Determining most likely exploitable technologies with AI...")
    exploitable_tech_analysis = determine_exploitable_technologies_with_ai(detected_tech, exploits_found)
    
    display_exploit_summary(detected_tech, exploits_found)
    print("\n AI Recommended Attack Surface:")
    print(exploitable_tech_analysis)
