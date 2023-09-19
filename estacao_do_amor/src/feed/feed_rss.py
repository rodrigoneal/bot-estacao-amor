import feedparser



url = "https://anchor.fm/s/e5566360/podcast/rss"    
def get_feed() -> dict[str, str]:
    feed = feedparser.parse(url)
    title = feed.entries[0].title
    summary = feed.entries[0].summary
    return {"title": title, "summary": summary}