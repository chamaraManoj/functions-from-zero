from wikibot import scrap

def test_scrap():
    assert "Microsoft" in scrap("Microsoft", 10)

