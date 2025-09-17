---
title: Introduction to tremendous-client
---

## A Python client library for the Tremendous API

A simple and lightweight client library for the Tremendous API. The <i>tremendous-client</i> provides convenient access to resources like orders, rewards, products, campaigns, funding sources, invoices, and more.

### What is Tremendous?

With Tremendous you can offer prepaid cards, money transfers, charitable donations, or let your customers choose from 2,100+ gift cards. Deliver instantly via SMS, email, and bulk link export. 

[Learn more about Tremendous](https://tremendous.com)


### Requirements

- Python 3.8+
- A Tremendous account and API Key. Get started with the [Sandbox here](https://developers.tremendous.com/docs/1-create-a-sandbox-account). 

### Installation

Install using pip 
```bash
pip install tremendous-client
```

...or clone directly from Github
 
```bash
git clone https://github.com/FreshNar/Tremendous-Python
```

### Never Hardcode Keys

Yeah, you’ll see API Key snippets sprinkled around these docs — they’re just placeholders, don’t actually use them. Treat your real keys like secrets (because they are). Hardcoding them into your codebase? Big no. Push them to GitHub? Game over.

If you want to do it the right way, stash your keys in environment variables or a secrets manager.

Consider using [python-dotenv](https://pypi.org/project/python-dotenv/) to store your API keys as enviornment variables.