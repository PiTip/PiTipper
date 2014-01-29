import unittest
import logging
import praw
import itertools

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)


class TestUpdate(unittest.TestCase):
    def setUp(self):
        # import configparser
        # config = configparser.ConfigParser()
        # config.read('example.ini')
        import os
        try:
            (self.user, self.password) = os.environ.get(
                'REDDIT_DSN', None).split(':')
        except:
            log.debug(
                '''Reddit connection details expected in''' + \
                '''os environ, e.g. REDDIT_DSN="username:password"''')
            raise Exception("No connection DSN")

    def tearDown(self):
        pass

    # @unittest.skip("Passed, skipping")
    def test_do_prawtest(self):
        r = praw.Reddit(
            'Pi DogeTipBot by /u/pitipper aka JC300. Source code is available.'
            )
        assert r is not None
        r.login(self.user, self.password)
        already_done = set()
        # Look for recent submissions in r/dogecoin
        for comment in itertools.islice(
                r.get_subreddit('dogecoin'
                    ).get_comments(), 10):
            log.debug("Doing comment id {0}".format(comment.id))
            for prawobj in [comment.submission.comments]:
                subcomments = [prawobj] \
                    if not isinstance(prawobj, list) else prawobj
                for subcomment in subcomments:
                    if subcomment.body == "Tip" \
                        and subcomment.id not in already_done:
                        log.debug("Reply to comment {0} ('+/u/Doge" + \
                                  "TipBot 31.415926 doge')".format(
                                subcomment.id))
                        already_done.add(subcomment.id)


if __name__ == '__main__':
    unittest.main(verbosity=2)
