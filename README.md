# Arxiv Paper Ranking Tool

This Python script fetches recent papers from specific fields on Arxiv and ranks them based on the number of clicks by researchers, utilizing data from https://papers.cool/. It aims to help users quickly find popular and potentially impactful research papers in their field of interest.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1QnxMmJtkoOBk4FPJXKi8Z-u8ldzOrtwr?usp=sharing)

**I strongly recommend you to use `colab` with two click to know the best papers in recent days!**

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
```

## Usage

Run the script from the command line, specifying the field using the `-f` or `--field` option. Only input one element from the list `['CL', 'LG', 'AI', 'CV']`. The default field is `CL`.

Example:

```bash
python paper_rank.py -f AI
```

This command fetches and ranks papers from the Artificial Intelligence (AI) field.

or

```bash
python paper_rank.py
```

This command fetches and ranks papers from the Computation and Language (CL) field.

## Output
The script prints the top 10 papers for each of the recent dates it fetched, sorted by the number of opens. Each paper's title and the total opens are displayed.

For example, running python paper_rank.py on 11/03/2024, we get:
```text
Date: 2024-03-11, URL: https://papers.cool/arxiv/cs.CL?date=2024-03-11&show=200
Top 10 Papers:
162 Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context
75 Tell, Don't Show!: Language Guidance Eases Transfer Across Domains in Images and Videos
49 Bayesian Preference Elicitation with Language Models
49 Bias-Augmented Consistency Training Reduces Biased Reasoning in Chain-of-Thought
41 Can't Remember Details in Long Documents? You Need Some R&R
38 Will GPT-4 Run DOOM?
35 RAT: Retrieval Augmented Thoughts Elicit Context-Aware Reasoning in Long-Horizon Generation
34 GEAR: An Efficient KV Cache Compression Recipefor Near-Lossless Generative Inference of LLM
32 To Err Is Human, but Llamas Can Learn It Too
30 Tell me the truth: A system to measure the trustworthiness of Large Language Models

--------------------------------------------------

(The other 3 days`data)

--------------------------------------------------

Date: 2024-03-05, URL: https://papers.cool/arxiv/cs.CL?date=2024-03-05&show=200
Top 10 Papers:
72 Not all Layers of LLMs are Necessary during Inference
59 Key-Point-Driven Data Synthesis with its Enhancement on Mathematical Reasoning
56 CLLMs: Consistency Large Language Models
40 IntactKV: Improving Large Language Model Quantization by Keeping Pivot Tokens Intact
35 Masked Thought: Simply Masking Partial Reasoning Steps Can Improve Mathematical Reasoning Learning of Language Models
30 Contrastive Region Guidance: Improving Grounding in Vision-Language Models without Training
27 You Need to Pay Better Attention
21 LLM-Oriented Retrieval Tuner
21 Rethinking LLM Language Adaptation: A Case Study on Chinese Mixtral
20 Infusing Knowledge into Large Language Models with Contextual Prompts

--------------------------------------------------
```
