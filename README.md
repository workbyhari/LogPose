# LogPose 

#### Video Demo:  https://youtu.be/nw2CaJ1ZMd4?si=rtdpXJmwCVROC-V7

#### Description:
The **LogPose** is a fast, command-line terminal program built as the final project for CS50’s Introduction to Programming with Python (CS50P). 

The goal of this project is to help users find high-quality movies and TV shows to watch based on their specific preferences. Instead of making slow requests over the internet, this program works completely offline by reading directly from the official IMDb data files (`title.basics.tsv.gz` and `title.ratings.tsv.gz`) stored right on your laptop. 

#### How the Code Works & Filters Data:
When you search through millions of rows of data, running unoptimized searches can make a computer freeze up. This program handles that data efficiently by splitting the filtering process into two clear stages:

1. **Reading the Basics File:** The program uses Python's built-in `gzip` and `csv` tools to read the compressed layout metadata. It looks at the user's preferred content type (like `movie` or `tvSeries`), year, and genre. If a title matches, the program saves its unique IMDb ID, name, and release year inside a fast Python dictionary.
2. **Matching the Ratings File:** Next, the program opens the ratings dataset. It checks the IDs directly against the saved dictionary. If a show matches your minimum rating target (using a greater-than-or-equal-to `>=` condition) and satisfies your minimum vote count, it is successfully added to your final recommendation list.

#### User Layout & Interface:
The application uses the `tabulate` library to print out all matching recommendations inside beautiful, organized terminal grid tables. To prevent the screen from getting filled with random home videos or unrated placeholder uploads, the program guides the user to set a recommended baseline of **500 minimum votes**. This allows the filters to surface great hidden gems, cult anime classics, and international hits seamlessly.

#### File Structure Breakdown:
- **`project.py`**: The main application file containing the primary execution loop alongside clean, modular functions: `chosen_type()`, `chosen_genre()`, `chosen_year()`, `chosen_votes()`, and `fetch_data()`.
- **`test_project.py`**: The unit testing file running on `pytest` to make sure our functions, input criteria validation, and error management loops work flawlessly without crashing.
- **`requirements.txt`**: A text file listing the external library dependency (`tabulate`) needed to display the output grids.
- **`README.md`**: This clear guide document explaining the project layout and user instructions.
-
-
