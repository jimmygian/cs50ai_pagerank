# CS50AI | Lecture 2 - Uncertainty | Project 2A - [PageRank](https://cs50.harvard.edu/ai/2024/projects/2/pagerank/)

This project is a mandatory assignment from **CS50AI – Lecture 2: "Uncertainty"**.

### 📌 Usage

To run the project locally, follow these steps:

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/yourusername/cs50ai-pagerank.git
   cd cs50ai-pagerank
   ```

2. **Run the program** by executing the following command:

   python pagerank.py [corpus]

   Replace `corpus` with the path to the directory containing the HTML files you wish to analyze.

<br>

## Project Overview

The goal of this project is to implement and compute **PageRank**, the algorithm used by Google to rank web pages. The project includes two different methods for estimating PageRank:

- **Sampling-based PageRank**: The program estimates the rank of a page by randomly sampling a large number of page visits according to a transition model.
- **Iterative-based PageRank**: The program uses an iterative method to update PageRank values until they converge.

This assignment provides hands-on experience in working with algorithms related to **uncertainty** and **randomness**.

### My Task

For this project, I implemented two core methods to compute PageRank:

1. **`sample_pagerank()`**: This function (along with `transition_model()`) computes the PageRank values by sampling `n` pages, where `n` is specified as `SAMPLES` (10,000 in this case). It starts with a randomly selected page and follows the transition model based on a damping factor (`DAMPING` = 0.85), updating the counts of visited pages.

2. **`iterate_pagerank()`**: This function computes PageRank values iteratively until the change in values between iterations is below a specified threshold (`THRESHOLD` = 0.001). The PageRank of each page is calculated using the formula:

   PR(p) = (1 - damping) / N + damping * Σ (PR(i) / NumLinks(i))


### Key Functions:

  
- **`transition_model()`**: This function computes a transition model representing the probability distribution over which page to visit next, based on the damping factor and outgoing links of the current page.

- **`sample_pagerank()`**: Estimates the PageRank values by sampling pages based on the transition model.

- **`iterate_pagerank()`**: Computes PageRank iteratively, updating the ranks until they converge.

<br>

## Conclusion

In this project, I implemented both sampling-based and iterative methods for computing PageRank. The sampling method relies on a probabilistic model and is useful for estimating ranks quickly by simulating random visits to pages. The iterative method, on the other hand, provides a more precise estimate by continually refining the ranks until convergence.

This assignment helped me understand the core concepts of **uncertainty** in algorithms, particularly how random sampling can be used to estimate values, and how iterative processes can be employed for optimization.

I also gained practical experience in parsing HTML files, handling data structures like dictionaries and sets, and applying algorithms to solve real-world problems in web search and ranking.
