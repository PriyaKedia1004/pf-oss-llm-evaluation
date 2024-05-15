# Bring your own Data QnA

This sample demonstrates Q&A application powered by Open source LLMs hosted on Azure Managed Online Endpoint. It utilizes indexed files from Azure Machine Learning to provide grounded answers. You can ask a wide range of questions related to Azure Machine Learning and receive responses. The process involves embedding the raw query, using vector search to find most relevant context in user data, and then using LLM to chat with you with the documents. This sample can also be used to evaluate LLMs on custom data using both pre-built and custom metrics like Groundedness, Relevance, GPT Similarity Score, F1 Score, BLEU Score, etc and select the model best suited for your use case.

## What you will learn

In this flow, you will learn

* how to compose a Q&A system flow.
* how to use vector search tool to find relevant documents and leverage domain knowledge.
* how to tune prompt with variants.

## Prerequisites

- Connection: Azure OpenAI or OpenAI connection, with the availability of chat/completion and embedding models/deployments.
- To perform batch run on this sample, you can download the sample data from <a href="https://ragsample.blob.core.windows.net/ragdata/QAGenerationData.jsonl" target="_blank">here</a>.

## Tools used in this flow

* LLM tool
* Embedding tool
* Vector Index Lookup tool
* Python tool

