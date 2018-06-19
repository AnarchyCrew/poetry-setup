"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject

Autogenerated by poetry-setup:
https://github.com/orsinium/poetry-setup
"""
# IMPORTANT: this file is autogenerated. Do not edit it manually.
# All changes will be lost after `poetry-setup` command execution.
# ----------------------------------------------------------------

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, '{{ package.readme.name }}'), encoding='utf-8') as f:
    long_description = f.read()


# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name='{{ package.name }}',  # Required
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/en/latest/single_source_version.html
    version='{{ package.version }}',  # Required
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="{{ package.description }}",  # Required
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    {% if package.homepage %}
        url="{{ package.homepage }}",  # Optional
    {% endif %}
    {% if package.author_name %}
        author="{{ package.author_name }}",  # Optional
    {% endif %}

    {% if package.author_email %}
        author_email="{{ package.author_email }}",  # Optional
    {% endif %}
    {% if package.all_classifiers %}
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        classifiers={{ package.all_classifiers|pprint }},  # Optional
    {% endif %}

    {% if package.keywords %}
        keywords=' '.join({{ package.keywords|pprint }}),  # Optional
    {% endif %}

    packages=find_packages(
        {% if package.exclude %}
        exclude=[
            {% for ex in package.exclude %}
                '{{ ex }}',
            {% endfor %}
        ]
        {% endif %}
    ),  # Required

    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        {% for req in package.all_requires %}
            {% if not req.is_optional() and not req.is_vcs() %}
                '{{ req.to_pep_508() }}',
            {% endif %}
        {% endfor %}
    ],  # Optional

    # https://setuptools.readthedocs.io/en/latest/setuptools.html#dependencies-that-aren-t-in-pypi
    dependency_links=[
        {% for req in package.all_requires %}
            {% if not req.is_optional() and req.is_vcs() %}
                '{{ format_vcs(req) }}',
            {% endif %}
        {% endfor %}
    ],  # Optional

    {% if package.extras %}
        extras_require={{ package.extras|pprint }},
    {% endif %}

    # NOT SUPPORTED YET
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    data_files=[],  # Optional

    {% if package.scripts %}
        entry_points={  # Optional
            'console_scripts': [
                {% for name, point in package.scripts.items() %}
                    '{{ name }}={{ point }}',
                {% endfor %}
            ],
        },
    {% endif %}

    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    project_urls={  # Optional
        {% if package.homepage %}
            'homepage': '{{ package.homepage }}',
        {% endif %}
        {% if package.repository %}
            'repository': '{{ package.repository }}',
        {% endif %}
        {% if package.documentation %}
            'documentation': '{{ package.documentation }}',
        {% endif %}
    },
)