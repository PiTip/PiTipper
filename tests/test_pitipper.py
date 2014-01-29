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
        subreddit = r.get_subreddit('dogecoin')
        comments = list(itertools.islice(subreddit.get_comments(), 10))
        for comment in comments:
            log.debug("Comment {0}".format(comment.id))
            subcomments = comment.submission.comments
            # Do unnested comments?
            for subcomment in [
                    sc for sc in subcomments if isinstance(
                        sc, praw.objects.Comment)]:
                try:
                    log.debug("Subcomment {0}".format(subcomment.id))
                    if subcomment.body == "Tip" \
                        and subcomment.id not in already_done:
                        log.debug(
                            "Reply to comment {0} ('+/u/Doge" + \
                                "TipBot 31.415926 doge')".format(
                                subcomment.id))
                        already_done.add(subcomment.id)
                except AttributeError as msg:
                    log.debug("Ooops {0}".format(msg))
            # Do flattened nested comments?
            for comment in praw.helpers.flatten_tree(comments):
                log.debug("Flattened Subcomment {0}".format(comment.id))
                if comment.body == "Tip" and comment.id not in already_done:
                    # comment.reply('+/u/DogeTipBot 31.415926 doge')
                    log.debug(
                        "Reply to comment {0} ('+/u/DogeTipBot" + \
                        " 31.415926 doge')".format(comment.id))
                    already_done.add(comment.id)
                    log.debug('Done!')
                else:
                    # Actually is error?
                    log.debug('Error')


if __name__ == '__main__':
    unittest.main(verbosity=2)
