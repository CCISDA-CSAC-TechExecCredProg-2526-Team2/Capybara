Search query syntax
===================

Read the Docs uses the `Simple Query String`_ feature from `Elasticsearch`_.
This means that as the search query becomes more complex,
the results yielded become more specific.

.. _Simple Query String: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-simple-query-string-query.html#
.. _Elasticsearch: https://www.elastic.co/products/elasticsearch

Exact phrase search
~~~~~~~~~~~~~~~~~~~

If a query is wrapped in ``"`` (double quotes),
then only those results where the phrase is exactly matched will be returned.

Examples:

- ``"custom css"``
- ``"adding a subproject"``
- ``"when a 404 is returned"``

Prefix query
~~~~~~~~~~~~

``*`` (asterisk) at the end of any term signifies a prefix query.
It returns the results containing the words with the specific prefix.

Examples:

- ``test*``
- ``build*``

Fuzziness
~~~~~~~~~

``~N`` (tilde followed by a number) after a word indicates edit distance (fuzziness).
This type of query is helpful when the exact spelling of the keyword is unknown.
It returns results that contain terms similar to the search term.

Examples:

- ``doks~1``
- ``test~2``
- ``getter~2``

Words close to each other
~~~~~~~~~~~~~~~~~~~~~~~~~

``~N`` (tilde followed by a number) after a phrase can be used to match words that are near to each other.

Examples:

- ``"dashboard admin"~2``
- ``"single documentation"~1``
- ``"read the docs policy"~5``
