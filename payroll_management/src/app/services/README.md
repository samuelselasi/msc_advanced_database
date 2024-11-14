# Services
This directory contains integration of useful services for the API that can be added to any of the routers at anytime, thus separated to easily add new implementations. 

Examples of such services are emails, payment gateways and other services that require third party configurations.

## Email Services

* `simple_send` -> set up to directly send emails on demand
* `send_in_background` -> set up to send emails as background tasks

