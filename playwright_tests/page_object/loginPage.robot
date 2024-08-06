*** Settings ***
Resource    ../resources/commons.robot

*** Variables ***
${URL}            https://www.casino777.be/

*** Keywords ***
Open Login Page
    Navigate To    ${URL}

Dismisses Didomi
   Click Button    id=didomi-notice-agree-button

Adds Cookies
   #I used a long XPATH, but thanks to Diana tips i changed it to something simpler
    Navigate To    https://www.casino777.be/qasecrettool
    Fill Input    input[name="dev_testIP"]    5.23.255.255
    Click Button   div:nth-child(5) > div > .transition-all

Triggers Login Popup
    Navigate To    ${URL}
    Click Button    data-testid=login-button-large
    Wait For Element to be Visible    id=username

Input Username
    [Arguments]    ${username}
    Type Input    id=username   ${username}

Input Password
    [Arguments]    ${password}
    Type Input    id=password   ${password}

Login
    [Arguments]    ${username}   ${password}
    Type Input    id=username    ${username}
    Type Input    id=password   ${password}
    Click Button    button[type="submit"]

Click Login Button
    Click Button    button[type="submit"]

Click Profile Button
    Click Button    .inline-flex

Wait For the Logged in Locator
    Wait For Element    data-testid=user-badge-indicator

Check If Cashier Exists
    Check the Element Existence  data-testid=user-controls-wrapper

Print Level Name
    [Documentation]    Prints the level of the current user.
    @{item_name}=    Get matching Elements Text    data-testid=user-badge-indicator
    Log to console    ${item_name}
    
Check If My Account Menu Present
     Wait Until Element Contains the Text    .ml-3  Mon compte

Click Logout Button
     #I used a long XPATH, but thanks to Diana tips i changed it to something simpler
     Click Button    //span[contains(text(), 'Se déconnecter')]

#Add All Items To Cart And Verify
 #   [Documentation]    Clicks all add-to-cart buttons and verifies the shopping cart badge count.
  #  ${click_count}=    Click on All Add To Cart Buttons    .btn_inventory
   # ${cart_badge_text}=    Get the Shopping Cart Badge Text    .shopping_cart_badge
    #Should Be Equal As Numbers    ${cart_badge_text}    6