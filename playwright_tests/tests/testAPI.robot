*** Settings ***
Resource   ../resources/commons.robot
Resource   ../page_object/apiPage.robot

*** Variables ***
${SESSION_NAME}              users
${BASE_URL}                  https://petstore.swagger.io/v2
${USER_ID}                    1
${USER_ID_TO_ADD}             12345
${USER_NAME_TO_ADD}           JohnQA
${FIRST_NAME_TO_ADD}          John
${LAST_NAME_TO_ADD}           Smith
${EMAIL_TO_ADD}               mihai@yopmail.com
${PASSWORD_TO_ADD}            sJgimo777
${PHONE_TO_ADD}               77777

*** Test Cases ***

Create User (POST)
    [Documentation]    A post request to create a new user
    Create API Session    ${BASE_URL}
    ${data}=    Create Dictionary   username=${USER_NAME_TO_ADD}  firstName=${FIRST_NAME_TO_ADD}  lastName=${LAST_NAME_TO_ADD}  email=${EMAIL_TO_ADD}  password=${PASSWORD_TO_ADD}  phone=${PHONE_TO_ADD}
    ${response}=     POST Request    /user    ${data}
    Should Be Equal As Numbers    ${response.status_code}    200

Get User Details (GET)
    [Documentation]    Perform a GET request to fetch user details.
    Create new API Session    ${BASE_URL}
    ${response}=     GET Request    /user/${USER_NAME_TO_ADD}
    Should Be Equal As Numbers    ${response.status_code}    200

Log in User
    [Documentation]    Logs in user
    Create API Session    ${BASE_URL}
    ${response}=     GET Request    /user/login?username=${USER_NAME_TO_ADD}&password=${PASSWORD_TO_ADD}
    TRY
         Should Be Equal As Numbers    ${response.status_code}    200
    EXCEPT
         Log to console    User does not exist. Try again.

    END

Perform PUT Request to update user details
    [Documentation]    Perform a PUT request to update pet details.
    Create API Session    ${BASE_URL}
    ${data}=    Create Dictionary   username=${USER_NAME_TO_ADD}  firstName=Andrei  lastName=${LAST_NAME_TO_ADD}  email=${EMAIL_TO_ADD}  password=${PASSWORD_TO_ADD}  phone=${PHONE_TO_ADD}
    ${response}=     PUT Request    /user/${USER_NAME_TO_ADD}    ${data}
    Should Be Equal As Numbers    ${response.status_code}    200

Log out User
    [Documentation]    Logs out user
    Create API Session    ${BASE_URL}
    ${response}=     GET Request    /user/logout
    TRY
         Should Be Equal As Numbers    ${response.status_code}    200
    EXCEPT
         Log to console    User does not exist. Try again.

    END

Perform DELETE Request to delete user
    [Documentation]    Perform a DELETE request to remove the pet.
    Create API Session    ${BASE_URL}
    ${response}=     DELETE Request    /user/${USER_NAME_TO_ADD}
    TRY
         Should Be Equal As Numbers    ${response.status_code}    200
    EXCEPT
         Log to console    User does not exist. Try again

    END
