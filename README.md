<h1>Cancun Hotel</h1>

### This application is designed to check the availability of hotel rooms in Cancun. Guests can also reserve a room of their preferred date, change booking details, and explore the website for some policies.

### The application to address all the requirements given to in the test.

### In order to access the whole website, the user has to do the following steps:

## Tutorial:

1. Sign-up
Fill in the form by typing a username, password, and email (optional).

2. If they chose to put their email address, the system will send a confirmation mail for verification.

3. Once they confirmed, they will be redirected to log-in section where they should enter their username and password.

4. Once logged-in, they will see their personal dashboard where they can access the whole website as a guest.

5. On the above panel, they can see the following buttons as seen on the screenshot below.

6. By clicking the "hotel button", available rooms will appear and the user can choose their preferred dates of stay. Note that it's not possible to book 30 days or more in advance of the current day.

7. Once they reserved a room, the details will be forwarded to "reservations section". So if they needed to make some changes, just click "reservations", then click update. From there, users can edit the date/ schedule of their booking.

8. To log out, simply click the button on the upper right corner which shows their username, then click log out.


For additional features on this site:

+ Security layer - such as (SECURE_HSTS_SECONDS, SECURE_HSTS_INCLUDE_SUBDOMAINS, SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER, SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE, CSRF_COOKIE_HTTPONLY, X_FRAME_OPTIONS)

+ Authentication

+ Log in and out

+ Changing of password

+ Confirmation mail after signing up

+ Admin system support- if troubleshooting is needed, the system will send or receive a notification that something has to be fixed.

+ Environment variables to protect secret information

+ Custom User

+ Application deployed in Heroku

## Technogies used:
<table>
    <tr>
        <td>Python</td>
        <td>Django</td>
        <td>Django Rest Framework</td>
        <td>Postgres</td>
        <td>Pytest</td>
    </tr>
    <tr>
        <td>3.8.7</td>
        <td>3.2</td>
        <td>3.12.4</td>
        <td>0.5.0</td>
        <td>7.1.2</td>
    </tr>
</table>