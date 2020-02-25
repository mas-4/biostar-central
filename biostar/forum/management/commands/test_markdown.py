import logging

from django.core.management.base import BaseCommand
from biostar.forum import markdown

logger = logging.getLogger('engine')

test = """

<b>foo</b>

1 > 0

    1 > 0 
 
"""


test2 = """

<b> foo </b>

1 > 0
<script> bar() </script>

    1 > 0 
    <b> bar </b>
    <script> bar() </script>

"""


test3 = """

<b> foo </b>

1 > 0
<script> bar() </script>

<code>
    1 > 0 
    <b> bar </b>
    <script> bar() </script>
</code>



"""

test4 = """

<b> foo </b>

1 > 0
<script> bar() </script>

<pre>
    <code>
        1 > 0 
        <b> bar </b>
        <script> bar() </script>
    </code>
</pre>


"""


gist_test = "https://gist.github.com/afrendeiro/6732a46b949e864d6803"


class Command(BaseCommand):
    help = 'Used to test markdown rendering'

    def handle(self, *args, **options):
        # import markdown2
        #
        # html_classes = dict(code="language-bash", pre="pre")
        # html1 = markdown2.markdown(test,
        #                            extras={"fenced-code-blocks": {},
        #                                   "code-friendly": {}, "nofollow": {}, "spoiler": {},
        #                                   "html-classes": html_classes})
        # print(html1)
        #print('MISTUNE', '-'*50)

        # escape = False to allow html in the markdown.
        html = markdown.parse(test, escape=False, clean=True, allow_rewrite=False)
        print()
        print(html)
