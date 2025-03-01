import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    # ranks = iterate_pagerank(corpus, DAMPING)
    # print(f"PageRank Results from Iteration")
    # for page in sorted(ranks):
    #     print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    TM = dict()
    N = len(corpus)  # Total number of pages

    # Get probability of random choice (1 page out of all N pages)
    random_choice = (1 / N) * (1 - damping_factor)

    # Get the outgoing links of the current page
    outgoing_links = corpus[page]

    if len(outgoing_links) == 0:
        # If there are no outgoing links, consider all pages as equal choice
        for potential_next_page in corpus:
            TM[potential_next_page] = random_choice
    else:
        # If there are outgoing links, distribute the damping factor over them
        for potential_next_page in corpus:
            if potential_next_page in outgoing_links:
                # The page has an outgoing link to this page
                TM[potential_next_page] = (1 / len(outgoing_links)) * damping_factor + random_choice
            else:
                # Otherwise, it's just the random choice
                TM[potential_next_page] = random_choice

    return TM


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Choose a page at random to start with
    page_visited = random.choice(list(corpus.keys()))
    visited_count = dict()

    # Repeat for n samples
    for _ in range(n):
        # Increment visit count for the current page
        if page_visited not in visited_count:
            visited_count[page_visited] = 1
        else:
            visited_count[page_visited] += 1

        # Get the transition model probabilities for the current page
        TM = transition_model(corpus, page_visited, damping_factor)
        
        # Get next random page based on the probabilities
        TM_pages = list(TM.keys())
        TM_values = list(TM.values())
        
        next_page = random.choices(TM_pages, weights=TM_values)[0]
        
        # Update the page visited
        page_visited = next_page

    # Normalize the visited count to estimate PageRank
    total_visits = sum(visited_count.values())
    for page in visited_count:
        visited_count[page] /= total_visits  # Normalize so the values sum to 1
    
    return visited_count


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
