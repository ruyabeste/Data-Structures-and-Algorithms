# 📘 Assignment #5 – Sphinx Documentation

This project demonstrates how to generate HTML documentation using **Sphinx** in Python. Below are the steps I followed, along with screenshots and notes.

### Setup Steps

1️⃣ Created docs/ folder and ran sphinx-quickstart

![Created docs](img/docs.png)

2️⃣ Answered configuration questions
I enabled separate source/build, set project name and author, and used English language.

![Questions](img/questions.png)

3️⃣ Installed Sphinx

![Install](img/pip_install.png)

4️⃣ Edited conf.py with autodoc

![Edit](img/edited.png)

5️⃣ Ran sphinx-apidoc to generate .rst files

![spinx](img/sphinx_apidoc.png)

6️⃣ Built HTML output using Alabaster theme

![built](img/make_html.png)

7️⃣ Viewed output in browser (Alabaster theme)

Opened index.html in the browser to verify output.

![open](img/other_theme.png)

8️⃣ Installed and tested sphinx_rtd_theme

pip install sphinx_rtd_theme

![Installtheme](img/pip_theme.png)

![Other_theme](img/sphinx.ext.autodoc.png)


| Theme           | Description                   | Preview                          |
|----------------|-------------------------------|----------------------------------|
| Alabaster       | Simple and clean              | ![Alabaster](img/other_theme.png) |
| sphinx_rtd_theme| Sidebar layout, modern look   | ![RTD](img/sphinx.ext.autodoc.png) |


✅ I preferred sphinx_rtd_theme because it offers better navigation and structure, especially for larger documentation.
