import feedparser
from feedparser.util import FeedParserDict

from estacao_do_amor.src.domain.schemas.podcast_schema import Episode, Podcast


class AnchorFeed:
    def __init__(self):
        self.url = "https://anchor.fm/s/e5566360/podcast/rss"
        self.feed_parser = self._parser_feed()

    def _parser_feed(self) -> FeedParserDict:
        return feedparser.parse(self.url)

    def podcast_episodes(self) -> Podcast:
        podcast = Podcast()
        for entrie in self.feed_parser.entries:
            episode = Episode(
                title=entrie["title"],
                link=entrie["link"],
                summary=entrie["summary"],
                published=entrie["published"],
                image=entrie["image"]["href"],
                audio=entrie["links"][-1]["href"],
                episode=entrie["itunes_episode"],
                season=entrie["itunes_season"],
                duration=entrie["itunes_duration"],
            )
            podcast.episodes.append(episode)
        return podcast

    def __repr__(self) -> str:
        return f"AnchorFeed(url={self.url})"
