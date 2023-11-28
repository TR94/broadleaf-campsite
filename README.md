# BroadLeaf Campsite

Welcome to BroadLeaf campsite in the heart of the picturesque Forest Of Dean. At BroadLeaf we have camping options that include Tent pitches, hard standing pitches and luxurious fully furnished glamping tents. Feel close to nature and explore the surrounding Forest steeped in history and ever changing scenery. 

This website has been developed to bring together the Full Stack techniques learnt on the Code Institute Full Stack Developer course and will be submitted for the Full Stack Portfolio Project. It focuses on using a framework (Django) and integrating back end functionality to a web page. 

<a href="https://github.com/users/TR94/projects/1" target="_blank">Link to the GitHub project</a>

<a href="https://broadleaf-booking-6b23cb1d45f9.herokuapp.com/" target="_blank">Link to the live site</a>

# User Experience

The target audience for this website is predominately people who want to get outdoors and camp in nature. The level of luxury and comfort varies between the users and therefore their requirements also vary. The website must be able to give the user the information for the campsite so they can decide whether or not the campsite fits their requirements.

## User personas:

Based on the offerings of the campsite, a set of user personas have been developed that capture the customer base likely to be attracted to the website. These user personas will be used to understand different customer perspectives and help guide the design of the website to make sure it is inclusive for the whole customer base.

- Offering 1: Tent pitch - User persona for someone who wants a tent pitch. <a href="https://res.cloudinary.com/dtgt7gfx7/image/upload/v1701211021/static/readme_files/Milly%20-%20Tent%20Pitch%20Persona.31987933122b.png" target="_blank">Tent pitch persona</a>
- Offering 2: Day van pitch - User persona for someone who wants somewhere to park their day van. <a href="https://res.cloudinary.com/dtgt7gfx7/image/upload/v1701211020/static/readme_files/Ricky%20and%20Sarah%20-%20Dayvan%20persona.ad47b19091db.png" target="_blank">Day Van persona</a>
- Offering 3: Caravan pitch - User persona for someone who wants somewhere to park their caravan. <a href="https://res.cloudinary.com/dtgt7gfx7/image/upload/v1701211022/static/readme_files/Smith%20family%20-%20caravan%20persona.3914d2a1ec49.png" target="_blank">Caravan persona</a>
- Offering 4: Motorhome/Campervan pitch - User persona for someone who wants to park their motorhome/campervan. <a href="https://res.cloudinary.com/dtgt7gfx7/image/upload/v1701211022/static/readme_files/Trevor%20and%20Amanda%20-%20Motorhome%20persona.68b8785b0a17.png" target="_blank">Motorhome persona</a>
- Offering 5: Glamping - User persona for someone who wants a luxury camping experience. <a href="https://res.cloudinary.com/dtgt7gfx7/image/upload/v1701211019/static/readme_files/Martin%20and%20Anna%20-%20Glamping%20persona.afefdb3457db.png" target="_blank">Glamping persona</a>

## Agile management 
The project will be managed with an Agile methodology. To cater for this GitHub projects has been used to track the progress of the project and manage each iteration and its subsequent tasks. The tasks are based around Epics and User Stories which are defined below for the BroadLead campsite project.

Initiative: Create a website to advertise Broadleaf camping site, take bookings and manage the pitches. 

User Groups: for this website there are two different user groups:
- “Admin” - campsite staff who need to interrogate the database to view and amend bookings 
- “Users” - customers who want to view the campsite and make a booking

Epic 1: The website needs an integrated booking system that'll allow users to:
- see availability and prices
- book specific items and dates
- take deposit payment
- send out confirmation email
- create an account to allow booking amendments
and allow admin to:
- see bookings 
- amend bookings 

User stories:\
Admin:
- As an admin, I want to be able to manually create bookings so I can serve customers who are having problems using the online booking system. (Create)\
Acceptance:
    - Successful creation of a new entry into the database 
    - Automatically sends confirmation of booking to the customer 
    - User is alerted if the booking has been unsuccessful 

- As an admin, I want to be able to view/read bookings so I can see which pitch customers have booked (view data)\
Acceptance:
    - Reqested data can be retrieved from the database in an easy to read format 
    - Successful requests should be able to be; pitch specific, name specific, campsite wide, time bound, etc

- As an admin, I want to be able to amend bookings (update or delete) so that I can move customers pitches or change the availability status of a particular pitch.\
Acceptance:
    - Successful update to the database, which demonstrates an information change to a booking. Changes must include:
    - Name(s) of guest(s)
    - Pitch number 
    - Date range 
    - Automatically sends confirmation of updates to the customer 
    - User is alerted if the updates are unsuccessful 

- As an admin, I want to be able to view booking trends so I can predict future business (reporting)\
Acceptance:
    - Reporting requirements to be defined 

Users:
- As a user, I want to be able to select the dates for my booking so I can make the booking\
Acceptance:
    - A date function is present for the user to interact with 
    - Dates not available are greyed out 

- As a user, I want to be able to choose the type of pitch for my booking so I can stay on the pitch I want\
Acceptance:
    - An interactive booking form that allows selection from a range of pitches 

- As a user, I want to see the availability of pitches so that I know if I can make a booking to meet my requirements.\
Acceptance:
    - Availability is displayed to the user in a clear fashion 
    - The availability displayed is the most is up to date from the database 

- As a user, I want to be able to make a booking to meet my requirements so I can plan the rest of my holiday\
Acceptance
    - Must have functionality for the user to make the booking based on their requirements:
        - Pitch type 
        - Check-in date
        - Check-out date
        - Number of guests
    - The booking must be entered into the database once it is made
    - The availability must change to "unavailable" for the specific details of the booking made 

- As a user, I want to be able to securely make a payment so I can secure my booking\
Acceptance:
    - Payment taken through a secure banking service (API)
    - Payment is taken for the correct amount 



- As a user, I want to receive confirmation of my booking so I can be sure it was made successfully\
Acceptance:
    - User receives confirmation of the payment and successful booking on the webpage 
    - User receives confirmation email with details of the booking 
    - User receives notification if that payment is unsuccessful


- As a user, I want a reminder near the check-in date of my booking so I can easily find the details in my inbox\
Acceptance:
    - Email reminder is sent to the customer with details of the booking, 1 week before Check-In date.
    - Admin are notified if reminder email is unsuccessfully delivered


Epic 2: The website needs to advertise the campsite and give the user the information they require such as:
- “Accommodation” options (yurt tent, hardstanding, pitch, etc..)
- Facilities 
- How to find the campsite 
- Contact details
- Booking options 
- Gallery to show off the site 
- Testimonials / reviews 

User stories:\
User:
- As a user, I want to be able to find the website on a search engine so I can find out more about the campsite (googlemaps, SEO, sponsored SEO)\
Acceptance:
    - Website has a relevant name which is searchable 
    - HTML data is relevant to increase SEO with search engines 
    - Consider sponsoring the site to boost placement in search results

- As a user, I want to be able to see the campsite grounds so I can judge whether or not I want to stay on the campsite\
Acceptance:
    - Must include photos of the campsite 
    - Gallery section for users to view all aspects of the site (facilities, pitches, scenery, etc)

- As a user, I want to be able to understand the different pitches available so I can decide whether or not it is suitable for my requirements\
Acceptance:
    - Information containing the pitches on offer 
    - Standardised layout of information for an improved user experience 

- As a user, I want to be able to see the facilities on offer so I can judge whether or not I want to stay on the campsite\
Acceptance:
    - Gallery section must include photos of the facilities 
    - Information containing the facilities must be included in the site for all types of users

- As a user, I want to be able to see where the campsite is located so I can decide whether or not it is suitable for my requirements\
Acceptance:
    - Include a Googlemap iframe on the contact page 
    - Include address on the contact page and footer 

- As a user, I want to be able to read reviews from other users so I can judge whether or not I want to stay on the campsite\
Acceptance:
    - Include link to reviews, to be determined from google reviews. 

- As a user, I want to be able to contact the campsite so I can have my questions answered\
Acceptance:
    - Contact details in the footer of each page
    - Contact page must include an email address and phone number 
    - Contact page to include a contact form

# Development Planes
In order to develop the website in an efficient and effective way, the 5 development planes have been considers. This incorporates the user stories and commercial needs of the site and focuses on developing a site that reaches the goals in the most efficient way. Working through the planes methodically should result in the first release of the site being much closer to the desired final output.

## Strategy
From a commercial aspect the branding and aesthetic of the site is key to how the campsite is perceive. The website must echo values that BroadLeaf want to associate with in order to attract a wide customer base. 

Business objectives:
The website must:
Introduce the brand 
Advertise the campsite and target search engine optimisation 
Show a natural experience with clean and modern facilities that engage a wide range of users
Target a customer base that has a range of needs

Booking system:
Must be able to manage bookings so that users can see availability and be able to book their requirements through the website. 

User requirements:
Be able to understand what the campsite has to offer
Find the location 
Be able to see availability and book pitches  

## Scope
Defining the scope at this stage allows a clear direction to be established before the detailed design starts.  

Based on the Strategy above, the content requirements will be based on the user stories. The functionality requirements will be wholly based on the booking system and how it manages to the availability of the campsite pitches. 

## Structure
Based on the strategy and scope above the site map shows a tree diagram of how the website will be constructed. This gives a brief overview of the pages and content:

![Site Map for BroadLeaf campsite](/static/readme_files/BroadLeaf_site_map.png)

From a database perspective the tables and relationships have been mapped out using the diagram below:

![Database model for BroadLeaf campsite](/static/readme_files/BroadLeaf_database_diagram.png)

## Skeleton
Wire-framing the pages in the early stages of design allows initial layouts and ideas to be visualised and edited easily without the need for coding. The building blocks of each page can be discussed and agreed upfront being committed to code. This approach allows the coding of the site to be much closer to final desired outcome which, in the long run, saves time and money.

Balsamic was used to create the following wireframes:

### Home Page: 
The Home page wireframes can be seen below, these consider the layout on a full size screen and a mobile screen:

![Home page wireframe full width](/static/readme_files/wireframe_home_desktop.png)

![Home page wireframe mobile width](/static/readme_files/wireframe_home_mobile.png)

### View bookings page:
Users will need to see the current bookings to check availability, the wireframes for full-size screens for this can be seen below. For mobile users the format will scale-down.

![View bookings wireframe full width](/static/readme_files/wireframe_view_bookings.png)

### About page:
The About page holds a lot of information for the site, this will be responsive to ensure it is mobile friendly. The layouts on a full size screen and a mobile screen can be seen below:

![About page wireframe full width](/static/readme_files/wireframe_about_desktop.png)

![About page wireframe mobile width](/static/readme_files/wireframe_about_mobile.png)

### Contact Page:
The Contact page wireframe can be seen below in mobile and desktop screen sizes:

![Contact page wireframe full width](/static/readme_files/wireframe_contact_desktop.png)

![Contact page wireframe mobile width](/static/readme_files/wireframe_contact_mobile.png)

At this stage, the wireframes are reviewed against the original strategy and goals of the project to ensure they’re aligned satisfactorily. This where the opportunity to 
There is an opportunity to circle back and update as required to achieve the desired output before coding begins.

## Surface

### Colour:
With any website, branding is a key aspect to consider and this extends to the colours used which associate to the brand. For BroadLeaf, the branding is kept simple and clean to not distract from the products on offer.

The light green (hex code: #90EE90) is the primary colour for BroadLeaf representing its ties to nature. This green is the core brand colour and using “color space” complementary colours were generated to add to the palette. These had to retain the natural/nature values of the brand but also give a modern feel without being distracting.

The final colour palette is:
Hex colour #FFFFFF, “white” used for background space 
Hex colour #90EE90,  “light green” used for the logo and footer banding
Standard body text colour (black) used for all text

![Colour pallette](/static/readme_files/palette_recommendation.png)

### Font:
For the logo, a modern and clean looking text is used. GoogleFonts provides “Roboto” in a regular 400 weight option.

It is important to pair the title font with a complementing style for the main body of the website. Font Joy was used to consider suggested font pairings and “Nunito Sans” was used, again in the regular 400 weight option.

These fonts have been included in the head of the base.html page through use of a content delivery network (CDN). The style.css file contains the font-family styling and has a “sans-serif” back up font in case of an error with the CDN link. 

### Images:
The images for the website are stored within the static/images folder. These have been sourced from Pexels and are open for free use. Images for the pitch offerings (Tent, Caravan, etc) are stored using cloudinary which is a separate cloud based storage area which is integrated into Django. 

### Icons:
The “BroadLeaf” logo is an icon from Font Awesome. Using a CDN, in the same way the fonts are loaded, Font Awesome’s library of icons are accessed with a link in the head element. This is exploited using the < i > tag and relevant class. 

Other icons are used throughout the page, mostly in the footer, to draw attention to specific areas of the page and improve the user experience. 

# Features

## Navigation and Logo
The logo and text: 
- BroadLeaf in the top left corner of the page show off the branding for the campsite and links to the home page as is traditional website convention. 
- The navigation links to navigate the site are in the top bar. These are Home, Book, About, Contact, Login and Register which link to their relevant sections of the site. 
- The font chosen is clean and modern with colours that are contrasting to ensure easy reading.
- The navigation links are consistent across the website which makes moving around the site easy and displays the information in a clear manner. For smaller screens, the nav bar shrinks to a hamburger icon to save space on the screen.

![Navigation bar screen grab](/static/readme_files/broadleaf_navbar.png)

## Content for the home page
- This section provides a clear overview of the campsite. 
- The header text is styled to continue the clean and simple theme.
- The image has been carefully chosen to allow an effective display responsive to different screen sizes.

![Header screen grab](/static/readme_files/broadleaf_home.png)

## About Us
Content meets the user stories explaining about the campsite and the facilities available 
Carousel of images to display the campsite 

![About-Us screen grab](/static/readme_files/broadleaf_about.png)

## Contact us 
Contact information and a location map
Contact form sent to an dedicated inbox

![Contact-Us screen grab](/static/readme_files/broadleaf_contact.png)

## The Footer
Contains branding, contact information and socials links

![Footer screen grab](/static/readme_files/broadleaf_footer.png)

## Booking
Current books table displays all bookings
Buttons to filter the bookings by date and pitch

![Bookings screen grab](/static/readme_files/broadleaf_view_bookings.png)

## My bookings
Views booking that are associated to the logged in user 
Can edit and cancel bookings that aren’t historical 

![My bookings screen grab](/static/readme_files/broadleaf_user_bookings.png)

## Edit booking
Form to edit the booking based on the current details 

![Edit booking screen grab](/static/readme_files/broadleaf_edit_booking.png)

## Cancel booking
Modal that asks for confirmation before cancelling the booking

![Cancel booking screen grab](/static/readme_files/broadleaf_cancel_booking.png)

## Features to add in the future
- Make the booking more interactive so there is feedback when the user is selecting dates to whether or not they are available such as a calendar which has green / red days
- Takes payment at the point of booking 
- Confirmation emails automatically sent for the booking  

# Technologies Used
**Coding languages used:**
- HTML5
- CSS3
- Python3\
**Frameworks:**
- Bootstrap 5
- Django 
- Psycopg2

## External resources used:
### Google Fonts:
Using a CDN link within the `<head>`, the font families “Roboto” and “Nunito sans” are used throughout the website. 

### Font Joy:
Used to pair the “Robot” logo font with a suitable body text font - this was “Nunito sans”.

### Font Awesome:
Using a CDN link within the `<head>`, icons are linked into the base.html template. These include the “BroadLeaf” logo icon as well as visual icons throughout the site (such as social media links).

### Am I Responsive?:
Used to test out how friendly the site is across various screen sizes. The responsive nature of the site is shown at the top of this document in the mock-up. 

### Balsamiq:
Wire-framing during the initial design of the website, used to easily edit the design ahead of initial agreement.

### Git-Hub / Git-Pod:
All project files are stored within a Git-hub repository.
Git-pod is linked into Git-hub through a browser extension and is the coding platform.

### Heroku 
With the pythonic nature of Django, Heroku is used to host the site as back-end application which can be interacted with. 

### Cloudinary
Cloud based storage for images and static files which remains stable to ensure links stay open indefinitely. 

# Accessibility 
Accessibility is a key consideration for any website which ensures the content is accessible to all. For this website the following aspects have been included:
- Aria labels on links to social media websites and navigation links 
- Alt labels on the images
- Using Chrome dev tools, the lighthouse score for this site is 97

![Lighthouse accessibility score](/static/readme_files/lighthouse_accessibility.png)

# Testing
## Manual Testing
### Functionality testing:

**Page loading:**\
Expected: Home page should load in the terminal with no errors\
Testing: type "python3 manage.py runserver” into the terminal\
Result: No errors reported with debug set to True. Page loads as expected.\
Fix: N/A

Expected: With page deployed, home page should load with no errors\
Testing: open page fro Heroku app\
Result: Images not displaying\
Fix: Update CSS to provide direct URLs to Cloudinary

**Home page:**\
Expected: Content is displaying as expected in mobile and desktop views\
Testing: Using Chrome Dev Tools, emulate each device and look for unexpected content displays\
Result: No issues\
Fix: N/A

**Register:**\
Expected: In full-screen view, using the nav-bar click on the “Register” link and takes you to the Sign-Up page\
Testing: Navigate to the “Register” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: In mobile view, using the collapsed nav-bar (hamburger) click on the “Register” link and takes you to the Sign-Up page\
Testing: Navigate to the “Register” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: Entering a blank username is presented with an error\
Testing: Sign-up with a blank username\
Result: Prompt given to enter a username\
Fix: N/A

Expected: To sign-up, a username can be entered using free-text\
Testing: Enter text into the username field\
Result: Text entered as expected\
Fix: N/A

Expected: A user name that has already been used is rejected with an error\
Testing: Enter an existing username\
Result: Error presented and told to sign-in instead\
Fix: N/A

Expected: Password entry doesn’t meet the defined requirements and an error is displayed\
Testing: Enter a poor password\
Result: Error presented with recommendations to improve the password\
Fix: N/A

Expected: Second password doesn’t match the first password and an error is displayed\
Testing: Enter a differing second password\
Result: Error presented with recommendations to improve the password\
Fix: N/A

Expected: Sign-in button creates a working log-in for the user\
Testing: Create a log-in\
Result: Log-in is met with a confirmation message\
Fix: N/A

Expected: Sign-in link navigates to the home page\
Testing: Create a log-in\
Result: Log-in is met with a confirmation message and redirected to home page\
Fix: N/A

Expected: Click the “Broadleaf logo” takes the user back to the home page\
Testing: Click the logo\
Result: Navigates to home page\
Fix: N/A

**Log-In and Log-Out:**\
Expected: In full-screen view, using the nav-bar click on the “Login” link and takes you to the Sign In page\
Testing: Navigate to the “Login” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: In mobile view, using the collapsed nav-bar (hamburger) click on the “Login” link and takes you to the Sign In page\
Testing: Navigate to the “Login” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: Entering a blank username is presented with an error\
Testing: Log-in with a blank username\
Result: Prompt given to enter a username\
Fix: N/A

Expected: To log-in, a username can be entered using free-text\
Testing: Enter text into the username field\
Result: Text entered as expected\
Fix: N/A

Expected: Entering a user name that hasn’t been registered is rejected with an error\
Testing: Enter incorrect log-in details\
Result: Error presented with prompt that log-in details are incorrect\
Fix: N/A

Expected: An incorrectly entered password is presented with an error\
Testing: Enter incorrect log-in details\
Result: Error presented with prompt that log-in details are incorrect\
Fix: N/A

Expected: Correct log-in credentials allow the user to log-in as expected\
Testing: Log-in with known credentials\
Result: Log-in successful with message displayed\
Fix: N/A

Expected: Upon logging in the user is redirected to the home page\
Testing: Log-in successfully\
Result: Redirected to home page\
Fix: N/A

Expected: Upon logging in the user is presented with a success message\
Testing: Log-in successfully\
Result: Success message displayed\
Fix: N/A

Expected: In full-screen view, using the nav-bar click on the “Logout” link and takes you to the Sign Out page\
Testing: Navigate to the “Logout” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: In mobile view, using the collapsed nav-bar (hamburger) click on the “Logout” link and takes you to the Sign Out page\
Testing: Navigate to the “Logout” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: The Sign Out page has a confirmation button to check sign-out was the desired action\
Testing: Logout redirects to confirmation page\
Result: Redirected as expected\
Fix: N/A

Expected: Sign-out button signs out the user as expected\
Testing: Click sign-out button\
Result: Signs out as expected\
Fix: N/A

Expected: After signing out the user is redirected to the home page\
Testing: Click sign-out button and redirect to home page\
Result: Redirected as expected\
Fix: N/A

Expected: After being redirect to the home page, user receives an on-screen message to confirm log-in\
Testing: Click sign-out button\
Result: Message displayed confirming successful sign-out\
Fix: N/A

**Booking App:**\
Expected: In full-screen view, using the nav-bar click on the “Book” link and takes you to the Booking page\
Testing: Navigate to the “Book” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: In mobile view, using the collapsed nav-bar (hamburger) click on the “Book” link and takes you to the Booking page\
Testing: Navigate to the “Book” button and click on it\
Result: Takes user to register page\
Fix: N/A

**My bookings:**\
Expected: Clicking the My Bookings button takes user to the “My bookings” page\
Testing: Click My Bookings button\
Result: Navigates to the “My bookings” page as expected\
Fix: N/A

Expected: Page can only be accessed by users who are logged in\
Testing: Click button without being logged in\
Result: Redirects to sign-in page\
Fix: N/A

Expected: Only the bookings of the logged in user are displayed in the table showing Pitch Type, Pitch ID, Date and duration\
Testing: Log-in as a user with out any bookings and no bookings will be displayed\
Result: No bookings displayed as expected\
Fix: N/A

Expected: Each row of current bookings (not in the past) table has a button to edit and cancel\
Testing: Check each row of bookings for buttons to edit and cancel\
Result: Historical buttons do not have the option to edit/cancel. All other bookings do.\
Fix: N/A

Expected: Clicking the edit button takes the user to the “Edit booking” page\
Testing: Click edit button\
Result: Takes to “Edit booking” page as expected\
Fix: N/A

Expected: Clicking the cancel button takes user to the “Cancel booking” page\
Testing: Click cancel button\
Result: Takes to “Cancel booking” page as expected\
Fix: N/A

Expected: Clicking the Book now button takes user to “Make booking” page\
Testing: Click Book Now button\
Result: Takes to “Make booking” page as expected\
Fix: N/A

**Edit booking:**\
Expected: Form pre-filled with information of the booking\
Testing: Click edit button and check information is pre-filled and correct\
Result: Information pre-filled and correct\
Fix: N/A

Expected: Able to edit the information as desired\
Testing: Edit dates/names/number of guests\
Result: Free to edit as desired\
Fix: N/A

Expected: Upon editing the booking, user is redirected to “view bookings” page\
Testing: Edit booking\
Result: Redirected to “view bookings” page as expected\
Fix: N/A

Expected: Upon editing the booking, user is presented with a success message\
Testing: Edit booking\
Result: No message displayed\
Fix: Add success message into the views.py for edit_booking

**Cancel booking:**\
Expected: Cancellation must require a confirmation before the action is completed\
Testing: Click cancel on a booking\
Result: Pop-up with a warning asking for confirmation of cancellation\
Fix: N/A

Expected: Upon cancelling the booking, user is redirected to “view bookings” page\
Testing: Cancelling booking\
Result: Redirected to “view bookings” page as expected\
Fix: N/A

Expected: Upon cancelling the booking, user is presented with a success message\
Testing: Cancelling booking\
Result: No message displayed\
Fix: Add success message into the views.py for cancel_booking

**View bookings:**\
Expected: View a list of current bookings for the campsite\
Testing: Create a range of bookings and confirm they are displayed\
Result: Bookings displayed in table as expected\
Fix: N/A

Expected: Current booking list must not have historical bookings presented\
Testing: Ensure old bookings are not visible\
Result: No historic bookings are present in the table\
Fix: N/A

Expected: List of bookings must be filterable by check in date and pitch ID\
Testing: Use date and Pitch ID and confirm filter is applied appropriately\
Result: Filters as expected\
Fix: N/A

Expected: Date filter input validation\
Testing: Add date in wrong format (DD-MM-YYYY)\
Result: Validation not available for this filter (filters.py), wrong format results in returning no results\
Fix: Cannot find fix to validate/control date input in django-filters. Workaround is to add the expected format above the filter for the user to follow.

Expected: There must be an explanation of how to use the page\
Testing: View page for explanation\
Result: Explanation in place\
Fix: N/A

**Make a booking:**
Expected: Page can only be accessed by users who are logged in\
Testing: Click “Book Now” booking without being logged in\
Result: Redirect to sign-in page\
Fix: N/A

Expected: First name field cannot be left blank\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: First name field will accept text\
Testing: Enter data into the field\
Result: Field accepts entry as expected\
Fix: N/A

Expected: Last name field cannot be left blank\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Last name field will accept text\
Testing: Enter data into the field\
Result: Field accepts entry as expected\
Fix: N/A

Expected: Pitch ID field displays the expected options\
Testing: Click drop down for pitch IDs\
Result: Pitch IDs displayed as expected\
Fix: N/A

Expected: Pitch ID field cannot be left blank\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Check-in-date field date picker allows easy option to pick the required date\
Testing: Click on date field and use date picker\
Result: Date selected as expected\
Fix: N/A

Expected: Check-in-date field will only accept a date format\
Testing: Submit form with invalid date\
Result: Cannot submit invalid date, date picker controls input\
Fix: N/A

Expected: Check-in-date field cannot be left blank\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Check-in-date field cannot be in the past\
Testing: Submit form with date in the past\
Result: Cannot submit invalid date, date picker controls input\
Fix: N/A

Expected: Check-out-date field date picker allows easy option to pick the required date\
Testing: Click on date field and use date picker\
Result: Date selected as expected\
Fix: N/A

Expected: Check-out-date field will only accept a date format\
Testing: Submit form with invalid date\
Result: Cannot submit invalid date, date picker controls input\
Fix: N/A

Expected: Check-out-date field cannot be left blank\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Check-out-date field cannot allow a date to be pick that is before the check-in-date\
Testing: Submit form with check out date being before check in date\
Result: Booking made successfully and duration displayed as a negative number\
Fix: To be implemented in next iteration; update logic in form submission to ensure check out date is greater than check in date.

Expected: Number of guests field must be a number only\
Testing: Field is controlled with a number picker\
Result: Can only enter a number. Number picker does allow a negative number to be chosen but an error message is displayed if a negative number of guests is submitted\
Fix: N/A

Expected: Number of guests field cannot less than or equal to zero\
Testing: Submit a number less than zero\
Number picker does allow a negative number to be chosen but an error message is displayed if a negative number of guests is submitted\
Fix: N/A

Expected: Number of guests field cannot be left blank\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Submit button allows user to submit booking\
Testing: Submit form\
Result: Booking submitted successfully\
Fix: N/A

Expected: Upon submitting booking form, user is redirected to the “view bookings” page\
Testing: Submit form\
Result: Redirected to view bookings page as expected\
Fix: N/A

Expected: Upon submitting booking form, user is presented with a success message\
Testing: Submit form\
Result: Success message displayed as expected\
Fix: N/A

Expected: If booking clashes with another booking, user is notified with an error message\
Testing: Create booking that clashes with another booking, ie. Same date and pitch ID.\
Result: Booking unsuccessful and error message displayed\
Fix: N/A

Expected: “Go-back” button takes user back to “view bookings” page\
Testing: Click “Go back” button\
Result: Navigates back to view bookings page\
Fix: N/A

**About Us:**\
Expected: In full-screen view, using the nav-bar click on the “About-Us” link and takes you to the About-Us page\
Testing: Navigate to the “About Us” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: In mobile view, using the collapsed nav-bar (hamburger) click on the “About-Us” link and takes you to the About-Us page\
Testing: Navigate to the “About Us” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: Content is displaying as expected in mobile and desktop views\
Testing: Using Chrome Dev Tools, emulate each device and look for unexpected content displays\
Result: No issues\
Fix: N/A

**Contact Us:**\
Expected: In full-screen view, using the nav-bar click on the “Contact-Us” link and takes you to the Contact-Us page\
Testing: Navigate to the “Contact Us” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: In mobile view, using the collapsed nav-bar (hamburger) click on the “Contact-Us” link and takes you to the Contact-Us page\
Testing: Navigate to the “Contact Us” button and click on it\
Result: Takes user to register page\
Fix: N/A

Expected: Content is displaying as expected in mobile and desktop views\
Testing: Using Chrome Dev Tools, emulate each device and look for unexpected content displays\
Result: No issues\
Fix: N/A

Expected: Google-map is displaying correctly, showing the correct address as expected\
Testing: View map and confirm correct address\
Result: Displaying as expected\
Fix: N/A

Expected: Google-map is interactive allowing the user to zoom in, zoom out and drag the map around.\
Testing: Use the map to zoom in, zoom out and move it around\
Result: Operates as expected\
Fix: N/A

**Contact form:**\
Expected: Contact form name field allows entry of free text\
Testing: Enter data into the field\
Result: Field accepts entry as expected\
Fix: N/A

Expected: Contact form name field left blank is presented with an error\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Contact form email field allows entry of free text\
Testing: Enter data into the field\
Result: Field accepts entry as expected\
Fix: N/A

Expected: Contact form email field left blank is presented with an error\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

Expected: Contact form email field entry isn’t an email is presented with an error\
Testing: Enter data without @ symbol\
Result: Error presented asking for an email address\
Fix: N/A

Expected: Contact form message field allows entry of free text\
Testing: Enter data into the field\
Result: Field accepts entry as expected\
Fix: N/A

Expected: Contact form message field left blank is presented with an error\
Testing: Submit form with field left blank\
Result: User prompted to fill in field\
Fix: N/A

### Responsive testing:
Using google dev tools, screen szies for mobile (Iphone XR), tablet (Ipad air), computer screen and larger screen (up to 1500px) the responsiveness for each page is tested.
Being built using Bootstrap, the website is created around a “mobile first” philosophy and therefore responsiveness is built-in. As an example the nav bar shrinks into a “hamburger” icon for small screens. 

### Validator Testing 
Validation testing using W3C Mark-Up Validation Service:
HTML for each page:
- base.html - only errors are jinja language based, not accepted by HTML checker
- index.html - only errors are jinja language based, not accepted by HTML checker
- edit_booking.html - only errors are jinja language based, not accepted by HTML checker
- make_booking.html - only errors are jinja language based, not accepted by HTML checker
- view_booking.html - only errors are jinja language based, not accepted by HTML checker
- my_booking.html - only errors are jinja language based, not accepted by HTML checker
- about.html - only errors are jinja language based, not accepted by HTML checker
- contact.html - only errors are jinja language based, not accepted by HTML checker
- style.css - no errors

CI Pep8 Python linter:
- booking.models.py - indentation errors only for fixing lines that are longer than 79 characters
- booking.views.py - indentation errors and lines to long for the template literal messages
- booking.forms.py - indentation errors only for fixing lines that are longer than 79 characters
- about.models.py - no errors
- about.views.py - no errors


# Bugs

## Solved bugs:
- Negative number of guests can be submitted. Fixed by adding a validator to the model. 
- Overlapping bookings. Initially booking logic was based on check in date however it didn’t check the dates after the check in date. Logic updated to check dates between a range. 
- CSS not linked after deployment. Had to relink the settings files and ensure config vars were correct in Heroku 
Main images not displaying after deployment. Fixed by changing the file path in the CSS file to a direct link to cloudinary

## Unfixed Bugs
Issues still remaining in the GitHub project:
- Editing a booking allows bookings to overlap, needs a check within the edit_booking view to make sure bookings are overlapping 
- Check out date can be before the check in date giving a negative duration of stay. View needs to have some logic added to make sure check out date is greater than check in date.

# Deployment 

The project was developed using GitPod and all changes were pushed to GitHub to keep a version history and store the code. The website is deployed using Heroku which provides a link to the website once it has been published. 

It is recommended to deploy the barebones of the project onto Heroku as soon as possible to ensure the connections have been made before the development begins.

### Local deployment is fro the Github repository using the following steps:
- Clone the repository from Github using the “Code” button (or if you have an extension to GitPod, click this)
- Open your IDE and link the Github repository to import the files
- Install the requirements for the site using `pip install -r requirements.txt`
- The application is built around environment variables which keep access keys secret for security purposes. This file will need to be created each time a local deployment is required because this file is not stored in the repository for security reasons. See Environment Variables for steps on how to do this. 
- With a database connected, make and run the migrations using `python3 manage.py makemigrations` and `python3 manage.py migrate`.
- The application requires a super user in order to access the admin area - this is created using the command `python3 manage.py createsuperuser`
- Products can be created within the admin panel using the “Products” section.
- Run the app using the `python3 manage.py runserver` command. Note, the local host address will need to be added to the “ALLOWED HOSTS” section within the settings.py file.


### Heroku deployment for public use:
- Login to your Heroku account and create a new app from the dashboard 
- Connect the GitHub repository to the Heroku app 
- Within the settings tab, set-up the environment variables in the Config Vars section.
- In the deploy tab, you can enable automatic deployments linked to the GitHub repository 
- Deploy the files using “Deploy branch” from main branch
- Once the app has finished building, click “View” to open the app. 

### Environment variables:
- For Heroku deployment the variables are stored in the Config Vars settings within the app.
- For local deployment, an env.py file is required to control the variables. 

To create the env.py the following variables are needed:
- URL to database 
- URL to cloudinary storage 
- Django secret key


# Credits 

Media:
- Images were taken from Pexels
Words:
- Bracelands campsite, Forest of Dean, for some home page wording
- ChatGPT for the "About-Us" wording

Code:
- W3Schools, Django documentation, Bootstrap 5 documentation and Stack Overflow helped with various coding challenges 
- See comments in the code for specific references

Acknowledgements:
- Thank you to my mentor, Seun, for her time, patience and guidance on the development of this website. 
- Thanks also are given to the Code Institute Slack Community who are always on hand to help at a moments notice.
- Thanks to the Code Institute tutor support who have been very persistent in helping with coding challenges throughout the project.