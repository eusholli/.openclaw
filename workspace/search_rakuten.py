import os
os.environ['TAVILY_API_KEY'] = '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'
from tavily import TavilyClient
client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])
response = client.search(query="Rakuten Symphony", search_depth="advanced", max_results=10)
import json
print(json.dumps(response, indent=2))