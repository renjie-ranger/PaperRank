# Arxiv Paper Ranking Tool

This Python script fetches recent papers from specific fields on Arxiv and ranks them based on the number of clicks by researchers, utilizing data from https://papers.cool/. It aims to help users quickly find popular and potentially impactful research papers in their field of interest.

## Features

- Fetches recent publication dates from Arxiv.
- Builds URLs to access papers from those dates on papers.cool.
- Sorts papers by the total number of opens (PDF and Kimi opens combined).

## Supported Fields

Currently, the script supports the following fields on Arxiv:

- Computational Linguistics (CL)
- Machine Learning (LG)
- Artificial Intelligence (AI)
- Computer Vision (CV)

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

Ensure you have the required packages installed by running:

```bash
pip install requests beautifulsoup4

## Usage

Run the script from the command line, specifying the field using the `-f` or `--field` option. Only input one element from the list `['CL', 'LG', 'AI', 'CV']`. The default field is `CL`.

Example:

```bash
python paper_rank.py -f AI

This command fetches and ranks papers from the Artificial Intelligence (AI) field.

or

```bash
python paper_rank.py

This command fetches and ranks papers from the Computation and Language (CL) field.

## Output
The script prints the top 10 papers for each of the recent dates it fetched, sorted by the number of opens. Each paper's title and the total opens are displayed.
