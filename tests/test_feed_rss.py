from datetime import datetime

from dateutil.tz import tzutc

from estacao_do_amor.src.feed.feed_rss import AnchorFeed


def test_se_pega_os_dados_do_feed():
    esperado = {
        "title": "EP. Piloto - Sobre AMOR",
        "link": "https://podcasters.spotify.com/pod/show/estao-do-amor/episodes/EP--Piloto---Sobre-AMOR-e28klk1",
        "published": datetime(2023, 8, 29, 0, 50, tzinfo=tzutc()),
        "audio": "https://anchor.fm/s/e5566360/podcast/play/75174977/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2023-7-28%2F801c2167-6075-5a9d-916c-ab24cb8d5241.mp3",
        "episode": 1,
        "season": 1,
        "duration": 1151,
        "image": "https://d3t3ozftmdmh3i.cloudfront.net/staging/podcast_uploaded_episode/38376440/38376440-1693243956446-85f70b24a28ca.jpg",
    }

    anchor_feed = AnchorFeed()
    podcast = anchor_feed.podcast_episodes()
    assert podcast.episodes[-1].model_dump(exclude=["summary"]) == esperado
