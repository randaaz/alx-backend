
```markdown
# 0x02. i18n

## Project Overview

This project involves setting up internationalization (i18n) for a Flask application. The primary goal is to learn how to parametrize Flask templates to display different languages, infer the correct locale based on URL parameters, user settings, or request headers, and localize timestamps.

### Learning Objectives
- Parametrize Flask templates for different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps.

### Requirements
- **Environment:** Ubuntu 18.04 LTS, Python 3.7
- **Coding Style:** Pycodestyle (version 2.5)
- **File Endings:** All files should end with a new line.
- **Shebang:** The first line of all Python files should be `#!/usr/bin/env python3`.
- **Executables:** All Python files should be executable.
- **Documentation:** Modules, classes, functions, and methods should have docstrings.
- **Type Annotations:** All functions and coroutines must be type-annotated.

## Tasks

### Task 0: Basic Flask App
- **Objective:** Set up a basic Flask app.
- **File:** `0-app.py`, `templates/0-index.html`
- **Description:** Create a single `/` route and an `index.html` template displaying "Welcome to Holberton" as the page title and "Hello world" as the header.

### Task 1: Basic Babel Setup
- **Objective:** Install and set up the Flask-Babel extension.
- **File:** `1-app.py`, `templates/1-index.html`
- **Description:** Install Flask-Babel, instantiate the Babel object, configure available languages (`["en", "fr"]`), set the default locale to `"en"` and timezone to `"UTC"`.

### Task 2: Get Locale from Request
- **Objective:** Create a `get_locale` function to determine the best match for supported languages.
- **File:** `2-app.py`, `templates/2-index.html`
- **Description:** Use `request.accept_languages` to determine the best match for supported languages.

### Task 3: Parametrize Templates
- **Objective:** Use `_` or `gettext` to parametrize templates.
- **File:** `3-app.py`, `babel.cfg`, `templates/3-index.html`, translations files
- **Description:** Create and compile translation dictionaries for English and French. Parametrize the templates using message IDs `home_title` and `home_header`.

### Task 4: Force Locale with URL Parameter
- **Objective:** Implement a way to force a particular locale using URL parameters.
- **File:** `4-app.py`, `templates/4-index.html`
- **Description:** Detect if the incoming request contains a `locale` argument and use it if it is a supported locale.

### Task 5: Mock Logging In
- **Objective:** Emulate a user login system.
- **File:** `5-app.py`, `templates/5-index.html`
- **Description:** Use a mock user table and implement a `get_user` function. Display a welcome message if a user is logged in.

### Task 6: Use User Locale
- **Objective:** Use the user's preferred locale.
- **File:** `6-app.py`, `templates/6-index.html`
- **Description:** Modify the `get_locale` function to prioritize locale from URL parameters, user settings, request headers, and default locale.

### Task 7: Infer Appropriate Time Zone
- **Objective:** Define a `get_timezone` function to infer the appropriate time zone.
- **File:** `7-app.py`, `templates/7-index.html`
- **Description:** Implement timezone detection logic and validate time zones using `pytz`.

---
