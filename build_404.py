# -*- coding: utf-8 -*-
from build import *

body_404 = '''
<section class="section" style="padding: 120px 0; text-align:center;">
  <div class="container">
    <span class="eyebrow">404</span>
    <h1>We couldn't find that page.</h1>
    <p style="margin:0 auto 28px;">The page you're looking for may have moved or no longer exists.</p>
    <a class="btn btn-primary" href="/index.html">Back to homepage</a>
  </div>
</section>
'''

write("404.html", page(
    "en", "", "", "",
    "Page not found | Cevano IT Solutions",
    "The page you're looking for could not be found.",
    "404.html", "404.html", body_404, alt_href="/pl/index.html"
))
