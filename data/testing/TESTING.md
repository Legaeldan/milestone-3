### Overall:

**Responsiveness-**

 - **Planning:**This project was required to be totally responsive, and mobile friendly as it would be intended to be used on the fly. hence the choice of Materialize as my main framework for it's cut down components that result in a clean, uncluttered view, with access to all features through hidden buttons and menus. Testing was done using dev-tools during the entire project, and also a final test of the entire site after completion.
 - **Testing:** Testing throughout the project was relatively simple using the materialize class modifiers. The only complicated issue in testing was the implimentation of the valign-wrapper, which was resolved by creating a class modifier, and implimenting a removal of the wrapper on discovery of this modifier.
 - **Defensive:** N/A
 - **Result:** A clean, responsive site, that works as expected. With no stray elements, or unwanted spacings.
 - **Verdict:** Test passed as expected and the site is responsive.

**Design**
 - **Planning:**Overal design had to be contrasting, to make specific elements jump out at the user. Colour charts to be created using [coolors.co](https://coolors.co/).
 - **Testing:**Multiple colour palettes were tested, and finally settled upon the final result. All version were shown to testers, and notes taken on favourites.
- **Result:** The overall theme of the site worked, and all tester were happy with the contrast.
- **Verdict:** Test passed, and overall design of the site works well together.

### Features:

**FAB Button**
 - **Planning:** A different approach to navigation of the site was needed. After some deliberation, a **Floating Action Button** was decided upon. This would have to be lightweight, smooth, and easy to use. With a stand out design to draw users to the icon.
 - **Testing (Phase 1):** During testing, multiple icons to reflect the menu item were tested. The final icons were then decided upon once in place.
 - **Testing (Phase 2):** During testing, it was found icons were not quite enough when using a desktop, as it wasn't quite as intuitive as using mobile. The icons were then accompanied by **Tooltips** when hovered. This gave a pleasant indication of each icon to the user. 
 - **Results:** The FAB works well, and was commented as being different and unique.
 - **Verdict:** Test passed, and the FAB works well in the context provided.

**Random Drink**
 - **Planning:** A search feature was needed to provide the user with a random document/drink from the database.
 - **Testing:** As this was tied into the view drink page, minimal testing was required. Tests were carried out using the **print()** funtion to ensure all results were indeed random, and follow the process through each step. After applying a random formula, was then applied to the view drink page. 
  - **Result:** A random drink/document is returned every time the link is viewed.
  - **Verdict:** Test passed, and feature works as expected.

**Logon System**
  - **Planning:** A logon feature was required to allow the user access to certain elevated functions.
  - **Testing (Phase 1):** A simple login system was implimented using a simple document repository for user details entered in forms.
  - **Planning (Revision):** Upon more research, it was found that data sent through the form could be intercepted. The decision to update the plan to include exryption to the logon system would be implimented using **bcrypt** encryption before passing data to the DB.
  - **Testing (Phase 2):** System was implimented, and reworked to integrate with the current system. Results in the database were then checked for encryption status. Multiple logons were created, and multiple variations of passwords were used on all to prove the system was secure.
  - **Result:** User is able to logon when using the correct details.
  - **Verdict:** Test passed, and feature works as expected.

**My Collection Page**
  - **Planning:** A feature to allow users to view only their own creations would be needed, so that users can maintain there own miniature database within the main database.
  - **Testing (Phase 1):** During testing, a simple, seperate page was created and tested with user details. Page returned only the currently logged in user drinks.
  - **Testing (Phase 2):** Refactoring of code meant that a single page could be utilised. The code was incorporated into the overall collection page, and upon testing was found to work both when a username was clicked, and when a URL was entered for a valid user.
  - **Results:** Users can obtain collections relating to specific users, and themselves upon request.
  - **Verdict:** Test passed, and feature is working as expected.

  **Switchable Menu**
  - **Planning:** A classic menu structure for users less familiar with the page, or the concept of a FAB menu.
  - **Testing (Phase 1):** Testing the toggle for the menu yielded promising results. During testing it was discovered that storage of the menu the user prefers needed to be held. Local storage via JS was implimented during this phase. The addition of a hide class was implimented to add and remove on certain clicks.
  - **Results:** User can toggle between menu styles, and option is persistent over multiple closures of browsers.
  - **Verdict:** Test passed as expected, and is working.

  **Add Drink/Edit Drink Modal**
  - **Planning:** A simple modal to add and edit drinks, reducing page switching. Creating a more streamline solution, and a neater layout overall.
  - **Testing (Phase 1):** Initial testing worked well, but was later discovered that the ingredient list did not generate for adding a drink if the logged in user had the ability to edit a drink. If the user was on one of their own creations, the loop that generates the list ended, and could not be iterated again.
  - **Testing (Phase 2):** A secondary retrieval of ingredients from the DB was implimented, and named specifically for a secondary modal. 
  - **Results:** After implimentation of a secondary loop, the modals populate correctly.
  - **Verdict:** Testing passed as expected.  

  **Drink Search**
  - **Planning:** A method to search drinks based on ingredients, so users can narrow results based on certain items contained in drink.
  - **Testing (Phase 1):** A simple list generated into a form facilitates searching the DB for a particular item. Search iterates over every ingredient on each drink, ensuring full coverage of all DB items. 
  - **Testing (Phase 2):** A secondary method was implimented from the view drink page. A simple way to return the above tests, but via clicking an ingredient link on the view drink ingredients section.
  - **Results:** User has multiple methods of searching for drinks based on an ingredient.
  - **Verdict:** All tests passed.
