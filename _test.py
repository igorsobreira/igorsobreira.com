'''
Tests for nginx configuration
'''

import requests

TEST_URL = 'http://igorsobreira.com'

# verify if all new pages are valid

def test_valid_pages():
    assert_valid('/', 'Blog posts')
    assert_valid('/2011/12/28/book-review-being-geek.html') # FIX BUG
    assert_valid('/posts.html', 'All posts')
    assert_valid('/talks.html', 'Talks')
    assert_valid('/atom.xml', '<feed xmlns="http://www.w3.org/2005/Atom">')

# verify all redirects from previous blog

def test_redirect_blog_index():
    assert_redirect('/blog/', '/')

def test_redirect_blog_post():
    assert_redirect('/blog/2010/9/6/blog-post/', '/2010/09/06/blog-post.html')
    assert_redirect('/blog/2010/10/6/blog-post/', '/2010/10/06/blog-post.html')
    assert_redirect('/blog/2010/9/16/blog-post/', '/2010/09/16/blog-post.html')
    assert_redirect('/blog/2010/10/26/blog-post/', '/2010/10/26/blog-post.html')

def test_redirect_static_pages():
    assert_redirect('/talks/', '/talks.html')
    assert_redirect('/books/', '/')
    assert_redirect('/about/', '/#about')
    assert_redirect('/contact-me/', '/#contact-me')

def test_redirect_feeds():
    assert_redirect('/blog/feeds/blog/rss/', '/atom.xml')
    assert_redirect('/blog/feeds/blog/atom/', '/atom.xml')
    assert_redirect('/blog/feeds/category/django/rss/', '/atom.xml')
    assert_redirect('/blog/feeds/category/python/atom/', '/atom.xml')

def test_redirect_category_page():
    # there is no more category page
    assert_redirect('/blog/category/pessoal/', '/posts.html')
    assert_redirect('/blog/category/linux/', '/posts.html')

def test_redirect_from_date_page():
    assert_redirect('/blog/2012/03/13/', '/posts.html')
    assert_redirect('/blog/2012/03/', '/posts.html')
    assert_redirect('/blog/2012/', '/posts.html')

def test_redirect_uploads():
    assert_redirect('/sitemedia/homepage/static-files/being-geek.jpeg', '/assets/uploads/being-geek.jpeg')

# asserts

def assert_valid(url, *expected_messages):
    resp = requests.get(TEST_URL + url)
    assert resp.status_code == 200, "Expected status 200 on %r but was %r" % (url, resp.status_code)
    for msg in expected_messages:
        assert msg in resp.content, "Expected body to contain %r" % msg

def assert_redirect(origin, target):
    resp = requests.get(TEST_URL + origin, allow_redirects=False)
    assert resp.status_code == 301, "Expected redirect from %r to %r, but response was %r" % (origin, target, resp.status_code)
    assert resp.headers['location'] == TEST_URL + target, "Expected redirect from %r to %r, but Location was %r" % (origin, target, resp.headers['Location'])
