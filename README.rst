=====
Aristotle MetaData Registry (Aristotle-MDR)
=====

|build-status| |docs| |coveralls| |demoserver|

Introduction and mission statement
----------------------------------
Aristotle-MDR is an open-source metadata registry as laid out by the requirements
of the `ISO/IEC 11179:2013 specification <http://metadata-standards.org/11179/>`_.

Aristotle-MDR represents a new way to manage and federate content built on and extending
the principles of leading metadata registries. The code of Aristotle is completely open-source,
building on the Django web framework and the mature model of the 11179 standard, allowing
agencies to easily run their own metadata registries while also having the ability
to extend the information model and tap into the permissions and roles of ISO 11179.

By allowing organisations to run their own independant registries they are able to
expose authoritative metadata along with the governance processes behind its creation,
and by building upon known and open systems agencies, can deliver a stable platform
for the sharing of metadata.

Extensions
++++++++++
Aristotle-MDR aims to be compliant to the core model described within ISO/IEC 11179,
however `a number of extensions are available to extend functionality and add additional content types <https://github.com/LegoStormtroopr/aristotle-metadata-registry/wiki/Available-Extensions>`_.


Quick start
-----------

1. Add "aristotle_mdr" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'haystack',
        'aristotle_mdr',
        'grappelli',
        ...
    )

   To ensure that search indexing works properly ``haystack`` **must** be installed before `aristotle_mdr`.
   If you want to take advantage of Aristotle's access-key shortcut improvements for the admin interface,
   make sure it is installed *before* ``grappelli``.

2. Include the Aristotle-MDR URLconf in your project ``urls.py``. Because Aristotle will
   form the majority of the interactions with the site, and the Aristotle includes a
   number of URLconfs for supporting apps its recommended to included it at the
   server root, like this::

    url(r'^/', include('aristotle_mdr.urls')),

3. Run ``python manage.py migrate`` to create the Aristotle-MDR Database.

4. (Optional) Compile the multilingual resource files for improved performance, like so::

     django-admin.py compilemessages

5. Start the development server and visit ``http://127.0.0.1:8000/``
   to see the home page.

For a complete example of how to successfully include Aristotle, see the `aristotle_mdr/tests/settings.py` settings file.

**A live Aristotle-MDR instance is available for review on PythonAnywhere at:** ``http://aristotle.pythonanywhere.com/``.
Be aware, this is an active development instance and may sporadically be unavailble.

Information for developers
--------------------------

Aristotle-MDR is free open-source software, and contributions are welcome on front-end web development,
back-end server development, translation and content creation (such as more documentation).
Review the wiki, open issues and existing documentation to get started.

About the badges (plus some extras):
++++++++++++++++++++++++++++++++++++
* |build-status| - Travis-CI, showing the details of the continuous testing suite
* |docs| - Rad the docs, with details on installing, configuring and extending Aristotle-MDR
* |coveralls| - Coveralls, showing in-depth code coverage
* |codecov| - Codecov.io, showing even more in-depther code coverage with branch coverage
* |demoserver| - A link to a live demo and development server
* |gitter| - Gitter, a git-powered chat room for developers


.. |build-status| image:: https://travis-ci.org/LegoStormtroopr/aristotle-metadata-registry.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/LegoStormtroopr/aristotle-metadata-registry

.. |docs| image:: https://readthedocs.org/projects/aristotle-metadata-registry/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://readthedocs.org/projects/aristotle-metadata-registry/

.. |coveralls| image:: https://coveralls.io/repos/LegoStormtroopr/aristotle-metadata-registry/badge.png?branch=master
    :alt: Code coverage on coveralls
    :scale: 100%
    :target: https://coveralls.io/r/LegoStormtroopr/aristotle-metadata-registry?branch=master

.. |codecov| image:: https://codecov.io/github/LegoStormtroopr/aristotle-metadata-registry/coverage.svg?branch=master
    :alt: Code coverage on code cov (includes branch checks)
    :scale: 100%
    :target: https://codecov.io/github/LegoStormtroopr/aristotle-metadata-registry?branch=master

.. |demoserver| image:: https://img.shields.io/badge/Demo_server-available-blue.svg
    :alt: visit the live demonstration server on PythonAnywhere
    :scale: 98%
    :target: http://aristotle.pythonanywhere.com

.. |gitter| image:: https://badges.gitter.im/Join%20Chat.svg
    :alt: visit the gitter chat room for this project
    :scale: 100%
    :target: https://gitter.im/LegoStormtroopr/aristotle-metadata-registry?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
