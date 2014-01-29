"""
Needs to be able to explore completely the subreddit "forest".
It's a graph, ofc.
"""

import unittest
import logging
import praw

log = logging.getLogger(__file__)
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)


class TestUpdate(unittest.TestCase):
    def setUp(self):
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

    @unittest.skip("Passed, skipping")
    def test_do_itertest(self):
        r = praw.Reddit(
            'Pi DogeTipBot by /u/pitipper aka JC300. Source code is available.'
            )
        assert r is not None
        r.login(self.user, self.password)
        already_done = set()
        # Look for recent submissions in r/dogecoin
        for comment in r.get_subreddit('dogecoin').get_comments(limit=10):
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

    @unittest.skip("Passed, skipping")
    def test_do_flatten_test(self):
        r = praw.Reddit(
            'Pi DogeTipBot by /u/pitipper aka JC300. Source code is available.'
            )
        r.login(self.user, self.password)
        already_done = set()
        # Look for recent submissions in r/dogecoin
        for comment in r.get_subreddit('dogecoin').get_comments(limit=6):
            log.debug("Doing comment id {0}".format(comment.id))
            for fcomment in praw.helpers.flatten_tree(
                    comment.submission.comments):
                # Not as flat as one might have expected
                if isinstance(fcomment, praw.objects.Comment):
                    if fcomment.body == "Tip" \
                        and fcomment.id not in already_done:
                        log.debug("Reply to comment {0} ('+/u/Doge" + \
                                  "TipBot 31.415926 doge')".format(
                                fcomment.id))
                        already_done.add(fcomment.id)
                elif isinstance(fcomment, praw.objects.MoreComments):
                    log.debug("Handle MoreComments")
                    # make repeated API calls to reddit
                    for scomment in fcomment.comments():
                        log.debug("Doing scomment id {0}".format(scomment.id))
                        if scomment.body == "Tip" \
                            and scomment.id not in already_done:
                            log.debug("Reply to comment {0} ('+/u/Doge" + \
                                      "TipBot 31.415926 doge')".format(
                                    scomment.id))
                            already_done.add(scomment.id)


if __name__ == '__main__':
    unittest.main(verbosity=2)
