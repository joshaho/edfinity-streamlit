# Master-Based Grading Generator (Streamlit

For a small side project, I needed a quick tool to ingest a standard format gradebook from [Edfinity](https://edfinity.com/) and convert it into binary grades as an input into an overall mastery-based grading scheme.

I got tired of constantly booting up a kernel to run this script locally, so instead used the opportunity to create a simple, [standalone streamlit application](https://share.streamlit.io/joshaho/edfinity-streamlit/main/edfinity_app.py) that would push out a processed CSV to reduce the amount of overhead for the task, and increase the reusability and opportunity for self-service.
