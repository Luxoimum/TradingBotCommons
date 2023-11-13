TradingBotIngestionService
==========================

|GitHub Actions|

.. |GitHub Actions| image:: https://github.com/Luxoimum/TradingBotIngestionService/workflows/main/badge.svg
   :target: https://github.com/Luxoimum/TradingBotIngestionService/actions
   :alt: GitHub Actions

Description
-----------

TradingBotIngestionService is a Job for data ingestion from Binance

Development and Testing
-----------------------

Requirements
~~~~~~~~~~~~

You will need `Python 3`_ and Poetry_ and Node.js_ with npm_.
To run some Serverless commands you will need Docker_.

Install the project dependencies

Using `PipX` for isolated environmental installation.

::
    $ brew install pipx

    $ pipx install poetry

Using regular global installation

::

    $ brew install pipx

    $ pipx install poetry

Using regular global installation

::

    $ pip install poetry

    $ apt install python3-poetry

    $ curl -sSL https://install.python-poetry.org | python3 -

.. _Docker: https://www.docker.com/
.. _Node.js: https://nodejs.org/
.. _npm: https://www.npmjs.com/
.. _Poetry: https://poetry.eustace.io/
.. _Python 3: https://www.python.org/

Quickstart
~~~~~~~~~~

::

    $ git clone https://github.com/Luxoimum/TradingBotIngestionService.git
    $ cd TradingBotIngestionService
    $ poetry install
    $ npm install

Run each command below in a separate terminal window:

::

    $ make watch

Primary development tasks are defined in the `Makefile`.

For executing script (environment variables are needed):

::

    $ export AWS_ACCESS_KEY_ID=<your_access_key>; \
    export AWS_SECRET_ACCESS_KEY=<your_secret_key>; \
    export AWS_DEFAULT_REGION=<your_region>; \
    export STOCK_MARKET_TABLE=<your_table_name>; \
    export STOCK_MARKET_INDEX=<your_table_index>; \
    python3 -m src.trading_bot_ingestion_service

Source Code
~~~~~~~~~~~

The `source code`_ is hosted on GitHub.
Clone the project with

::

    $ git clone https://github.com/Luxoimum/TradingBotIngestionService.git

.. _source code: https://github.com/Luxoimum/TradingBotIngestionService

Tests
~~~~~

Lint code with

::

    $ make lint


Run tests with

::

    $ make test

Run tests on changes with

::

    $ make watch

Publishing
~~~~~~~~~~
TBD

Deployment
~~~~~~~~~~

Serverless deployment is triggered by a release repository_dispatch on GitHub Actions.

Deployment may be triggered using a `release workflow_dispatch on GitHub Actions`_.

.. _release workflow_dispatch on GitHub Actions: https://github.com/Luxoimum/TradingBotIngestionService/actions?query=workflow%3Arelease

GitHub Actions
--------------

*GitHub Actions should already be configured: this section is for reference only.*

The following repository secrets must be set on GitHub Actions.

- ``PYPI_API_TOKEN``: API token for publishing on PyPI.
- ``AWS_DEFAULT_REGION``: The AWS region Serverless will deploy to.
- ``AWS_ACCESS_KEY_ID``: AWS access key ID.
- ``AWS_SECRET_ACCESS_KEY``: AWS secret access key.
- ``GH_TOKEN``: A personal access token that can trigger workflows.

These must be set manually.

Secrets for Optional GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The version and format GitHub actions
require a user with write access to the repository.
including access to trigger workflows.
Set these additional secrets to enable the action:

- ``GH_TOKEN``: A personal access token for the user.
- ``GIT_USER_NAME``: The name to set for Git commits.
- ``GIT_USER_EMAIL``: The email to set for Git commits.
- ``GPG_PRIVATE_KEY``: The `GPG private key`_.
- ``GPG_PASSPHRASE``: The GPG key passphrase.

.. _GPG private key: https://github.com/marketplace/actions/import-gpg#prerequisites

Contributing
------------

Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://github.com/Luxoimum/TradingBotIngestionService/fork).
2. Create your feature branch (`git checkout -b my-new-feature`).
3. Make changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin my-new-feature`).
6. Create a new Pull Request.

License
-------

This Serverless project is licensed under the MIT license.

Warranty
--------

This software is provided by the copyright holders and contributors "as is" and
any express or implied warranties, including, but not limited to, the implied
warranties of merchantability and fitness for a particular purpose are
disclaimed. In no event shall the copyright holder or contributors be liable for
any direct, indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services;
loss of use, data, or profits; or business interruption) however caused and on
any theory of liability, whether in contract, strict liability, or tort
(including negligence or otherwise) arising in any way out of the use of this
software, even if advised of the possibility of such damage.
