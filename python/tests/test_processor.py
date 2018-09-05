from lib.processor import top_resources

INPUT_1 = """
  [01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298
  [01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
"""

INPUT_2 = """
  [01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298
  [01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall2.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall3.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall4.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall5.gif HTTP/1.0" 200 3631
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall6.gif HTTP/1.0" 200 3632
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall7.gif HTTP/1.0" 200 3633
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall8.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall5.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall5.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall4.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall4.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall34.gif HTTP/1.0" 200 3635
  [01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall35.gif HTTP/1.0" 200 3635
"""

def test_with_few_logs():
    resources = top_resources(INPUT_1)
    assert len(resources) == 2
    assert resources[0] == ('/images/ksclogosmall.gif', (3, 10905))
    assert resources[1] == ('/images/opf-logo.gif', (2, 65022))

def test_with_more_than_10_logs():
    resources = top_resources(INPUT_2)
    assert len(resources) == 10
    assert resources[0] == ('/images/ksclogosmall.gif', (3, 10905))
    assert resources[1] == ('/images/ksclogosmall4.gif', (3, 10905))
    assert resources[2] == ('/images/ksclogosmall5.gif', (3, 10901))
    assert resources[3] == ('/images/opf-logo.gif', (2, 65022))
    assert resources[4] == ('/images/ksclogosmall2.gif', (1, 3635))
    assert resources[5] == ('/images/ksclogosmall3.gif', (1, 3635))
    assert resources[6] == ('/images/ksclogosmall34.gif', (1, 3635))
    assert resources[7] == ('/images/ksclogosmall35.gif', (1, 3635))
    assert resources[8] == ('/images/ksclogosmall8.gif', (1, 3635))
    assert resources[9] == ('/images/ksclogosmall7.gif', (1, 3633))
