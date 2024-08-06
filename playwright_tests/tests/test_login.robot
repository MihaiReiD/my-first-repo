*** Settings ***
Resource   ../resources/commons.robot
Resource   ../page_object/loginPage.robot

Test Teardown    Run keywords   Capture final Screenshot   AND   Close Playwright Browser
Test Setup     Run keywords   Open Playwright Browser
*** Variables ***
${USERNAME}       test_sanity2407
${PASSWORD}       sJgimo777

*** Test Cases ***
Login/Logout testcase
    [Documentation]    Test case where user logs in to the website and logs out
    Open Login Page
    Dismisses Didomi
    Adds Cookies
    Retry the Keyword    Triggers Login Popup    4
    Wait For Page to Load
    Input Username    ${USERNAME}
    Input Password    ${PASSWORD}
    Click Login Button
    Wait For Page to Load
    Wait For the Logged in Locator
    Check If Cashier Exists
    Print Level Name
    Click Profile Button
    Retry the Keyword    Check If My Account Menu Present   3
    Click Logout Button
    Wait For Element to be Visible    data-testid=login-button-large
    Assert the Element Text    data-testid=login-button-large   Connexion


Iterate through all elements
    [Documentation]    Test case to print all items name
    Open Login Page
    Login  ${USERNAME}   ${PASSWORD}
    Print All Item Names


Add everything to cart
    Open Login Page
    Login  ${USERNAME}   ${PASSWORD}
    Add All Items To Cart And Verify

