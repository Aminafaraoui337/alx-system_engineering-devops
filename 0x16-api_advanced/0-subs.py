import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API to get the number of subscribers for a given subreddit.
    If the subreddit is invalid or an error occurs, return 0.
    """
    try:
	req = requests.get(
	    f"https://www.reddit.com/r/{subreddit}/about.json",
	    headers={"User-Agent": "Custom"},
	    allow_redirects=False  # Prevents following redirects
	)
    if req.status_code == 200:
        return req.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
    except requests.RequestException:
        return 0
