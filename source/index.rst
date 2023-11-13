.. Curs Doc as Code documentation master file, created by
   sphinx-quickstart on Tue Oct 17 18:59:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

OpenAI ChatBot API documentation!
============================================

**Sergiu Stavila**

*/healthcheck* route
--------------------
**Return chatbot health status** 

- **HTTP Method**
  - Http GET Method

- **Response Codes**
  - A healthy response returns 200 OK status code.
  - An unhealthy response returns 500 Internal Server Error.

- **Response Body**
  - A healthy response looks like: "status": "Chatbot is healthy".
  - An unhealthy response might include details about the error, e.g., "status": "Error", "message": "Internal server error".

*/version* route
--------------------
**Returns the version of the chatbot stored in a VERSION file** 

- **HTTP Method**
  - Http GET Method

- **Response Codes**
  - A healthy response returns 200 OK status code.
  - An unhealthy response returns 500 Internal Server Error.

- **Response Body**
  - A healthy response looks like: "version": "1.0.0".
  - An unhealthy response might include details about the error, e.g., "status": "Error", "message": "Internal server error".

*/message* route
--------------------
**Connects to OpenAI API and is used to answer to questions** 

- **HTTP Method**
  - Http POST Method

- **Response Codes**
  - A healthy response returns 200 OK status code.
  - An unhealthy response returns 500 Internal Server Error.

- **Response Body**
  - A healthy response looks like: "status": "Chatbot is healthy".
  - An unhealthy response might include details about the error, e.g., "status": "Error", "message": "Internal server error".
