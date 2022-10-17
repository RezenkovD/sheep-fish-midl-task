### Libs installation
```bash
pip3 install -r requirements.txt
```

### TASK
1) The service receives information about a new order, creates checks for everyone in the database
point printers created in the order and puts asynchronous tasks on
generation of PDF files for these checks. If the point does not have any printer -
returns an error. If receipts for this order have already been created -
returns an error (the order number is passed).
2) An asynchronous worker using wkhtmltopdf generates a PDF file from
HTML template. The file name should look like order_id_type
check.pdf (123456_client.pdf). The files should be saved in the media/pdf folder in
the roots of the project.
3) The program polls the service for new checks. The survey is taking place
in the following way: first, a list of checks that have already been generated for
specific printer, after downloading the PDF file for each check and
sent to print. (this is the type of printer that changes the status in the second check)

Description:
The chain of delivery restaurants "Priest Top" has many points where food is prepared
orders for customers. Every customer wants to receive a receipt with the order
contains detailed information about the order. The kitchen staff also want the check,
so that in the process of preparing and packing the order, you don't forget to put everything
necessary. Our task is to help both by writing a service for generation
checks

### Technical requirements
1) The service must be written in python and Django
2) Database - PostgreSQL
3) All infrastructure things needed for the service (PostgreSQL, Redis, wkhtmltopdf)
run in docker using docker-compose, the project itself is not needed rotate in docker.
4) In addition to the API, there should be an admin for both models, with the ability to filter checks by
printer, type and status

### Notes
1) Layout of HTML templates for checks is in the repository in the templates folder
2) For ease of working with wkhtmltopdf, you should use a docker container wkhtmltopdf