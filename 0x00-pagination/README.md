# 0x00. Pagination

## Back-end

### Project Details
- **Start Date:** Jun 20, 2024, 6:00 AM
- **End Date:** Jun 25, 2024, 6:00 AM
- **Checker Release:** Jun 21, 2024, 12:00 PM
- **Auto Review:** Launched at the deadline

### Resources
- **Read or Watch:**
  - [REST API Design: Pagination](#)
  - [HATEOAS](#)

### Learning Objectives
By the end of this project, you should be able to explain the following without external help:
- How to paginate a dataset with simple `page` and `page_size` parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method
- All your functions and coroutines must be type-annotated

### Setup
- Use the `Popular_Baby_Names.csv` data file for your project

### Tasks

#### 0. Simple Helper Function
- Write a function named `index_range` that takes two integer arguments `page` and `page_size`.
- The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
- Page numbers are 1-indexed, i.e., the first page is page 1.

#### 1. Simple Pagination
- Copy `index_range` from the previous task and create a `Server` class to paginate a database of popular baby names.
- Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.
- Use assertions to verify that both arguments are integers greater than 0.
- Use `index_range` to find the correct indexes to paginate the dataset and return the appropriate page of the dataset.
- If the input arguments are out of range for the dataset, an empty list should be returned.

#### 2. Hypermedia Pagination
- Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing:
  - `page_size`: the length of the returned dataset page
  - `page`: the current page number
  - `data`: the dataset page (equivalent to the return from the previous task)
  - `next_page`: number of the next page, `None` if no next page
  - `prev_page`: number of the previous page, `None` if no previous page
  - `total_pages`: the total number of pages in the dataset as an integer

#### 3. Deletion-Resilient Hypermedia Pagination
- Implement a `get_hyper_index` method with two integer arguments: `index` with a default value of `None` and `page_size` with default value of 10.
- The method should return a dictionary with the following key-value pairs:
  - `index`: the current start index of the return page.
  - `next_index`: the next index to query with.
  - `page_size`: the current page size
  - `data`: the actual page of the dataset
- Ensure the method is deletion-resilient by maintaining consistency in paginated results even if rows are deleted between queries.

### Repository
- **GitHub Repository:** `alx-backend`
- **Directory:** `0x00-pagination`

Ensure all tasks are implemented as specified, with proper documentation and type annotations. Good luck!

